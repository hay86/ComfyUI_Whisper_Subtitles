# ComfyUI Whisper

Transcribe audio and add subtitles to videos using [Whisper](https://github.com/openai/whisper/) in [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

![demo-image](https://github.com/yuvraj108c/ComfyUI-Whisper/blob/assets/recording.gif?raw=true)

## Installation

1. Clone this repo into `custom_nodes` folder
2. Install dependencies: `pip install -r requirements.txt`
3. Install [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)

## Usage

Load this [workflow](https://github.com/yuvraj108c/ComfyUI-Whisper/blob/master/example_workflows/whisper_video_subtitles_workflow.json) into ComfyUI

## Nodes

### Apply Whisper

Transcribe audio and get timestamps for each segment and word.

### Add Subtitles To Frames

Add subtitles on the video frames. You can specify font family, font color and x/y positions.

### Add Subtitles To Background (Experimental)

Add subtitles like wordcloud on blank frames

## Credits

- [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)

- [Kosinkadink/ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite)

- [melMass/comfy_mtb](https://github.com/melMass/comfy_mtb)
