from .apply_whisper import ApplyWhisperNode
from .add_subtitles_to_frames import AddSubtitlesToFramesNode
from .add_subtitles_to_background import AddSubtitlesToBackgroundNode
from .resize_cropped_subtitles import ResizeCroppedSubtitlesNode

NODE_CLASS_MAPPINGS = { 
    "D_Apply_Whisper" : ApplyWhisperNode,
    "D_Add_Subtitles_To_Frames": AddSubtitlesToFramesNode,
    "D_Add_Subtitles_To_Background": AddSubtitlesToBackgroundNode,
    "D_Resize_Cropped_Subtitles": ResizeCroppedSubtitlesNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
     "D_Apply_Whisper" : "Apply Whisper", 
     "D_Add_Subtitles_To_Frames": "Add Subtitles To Frames",
     "D_Add_Subtitles_To_Background": "Add Subtitles To Background",
     "D_Resize_Cropped_Subtitles": "Resize Cropped Subtitles"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']