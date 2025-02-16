import whisper
import os
import folder_paths
import uuid
import torchaudio
import re


class ApplyWhisperNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "audio": ("AUDIO",),
                "model": (["base", "tiny", "small", "medium", "large"],),
            },
            "optional": {
                "known_text": ("STRING", {"default": '', "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING", "whisper_alignment", "whisper_alignment")
    RETURN_NAMES = ("text", "segments_alignment", "words_alignment")
    FUNCTION = "apply_whisper"
    CATEGORY = "whisper"

    def apply_whisper(self, audio, model, known_text=''):

        # save audio bytes from VHS to file
        temp_dir = folder_paths.get_temp_directory()
        os.makedirs(temp_dir, exist_ok=True)
        audio_save_path = os.path.join(temp_dir, f"{uuid.uuid1()}.wav")
        torchaudio.save(audio_save_path, audio['waveform'].squeeze(
            0), audio["sample_rate"])

        # transribe using whisper
        model = whisper.load_model(model)
        result = model.transcribe(audio_save_path, word_timestamps=True)

        segments = result['segments']
        segments_alignment = []
        words_alignment = []

        if known_text == '':
            for segment in segments:
                # create segment alignments
                segment_dict = {
                    'value': segment['text'].strip(),
                    'start': segment['start'],
                    'end': segment['end']
                }
                segments_alignment.append(segment_dict)

                # create word alignments
                for word in segment["words"]:
                    word_dict = {
                        'value': word["word"].strip(),
                        'start': word["start"],
                        'end': word['end']
                    }
                    words_alignment.append(word_dict)

            return (result["text"].strip(), segments_alignment, words_alignment)
        else:
            def clean_word(word):
                # 转换为小写，并使用正则表达式去除前后非字母数字字符
                return re.sub(r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$', '', word.lower())

            final_text = []
            search_start = 0
            known_text_words = known_text.split()
            known_text_words_key = [clean_word(word) for word in known_text_words]

            for segment in segments:
                segment_text = segment['text'].strip()
                segment_start = segment['start']
                segment_end = segment['end']

                # 提取 segment 中的单词
                words = segment['words']
                corrected_words = []

                for word in words:
                    word_text = word['word'].strip()
                    word_text_key = clean_word(word_text)

                    matched_len = 1
                    for i in range(-3, 3):
                        if search_start + i >= 0 and search_start + i < len(known_text_words_key):
                            if word_text_key == known_text_words_key[search_start + i]:
                                matched_len = 0 if i < 0 else max(matched_len, i+1)
                                break
                    
                    if matched_len == 0:
                        words_alignment[-1]['end'] = word['end']
                    else:
                        corrected_word = ' '.join(known_text_words[search_start+i] for i in range(matched_len) if search_start+i < len(known_text_words))
                        word_dict = {
                            'value': corrected_word,
                            'start': word['start'],
                            'end': word['end']
                        }
                        search_start += matched_len
                        words_alignment.append(word_dict)
                        corrected_words.append(corrected_word)

                # 使用修正后的单词更新 segment_text
                corrected_segment_text = ' '.join(corrected_words)

                segment_dict = {
                    'value': corrected_segment_text,
                    'start': segment_start,
                    'end': segment_end
                }
                segments_alignment.append(segment_dict)
                final_text.append(corrected_segment_text)

            return ' '.join(final_text), segments_alignment, words_alignment
        

