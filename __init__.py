"""LTX2.3 Frames Prompt — ComfyUI custom node for video prompt generation."""

from .nodes import ZhenzhenPrompt

NODE_CLASS_MAPPINGS = {
    "ZhenzhenPrompt": ZhenzhenPrompt,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ZhenzhenPrompt": "zhenzhen-prompt",
}

