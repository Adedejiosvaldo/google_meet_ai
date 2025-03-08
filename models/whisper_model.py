from faster_whisper import WhisperModel
import torch

class WhisperModelWrapper:
    def __init__(self, model_size="large-medium"):
        self.model = WhisperModel(
            model_size,
            device="cuda" if torch.cuda.is_available() else "cpu",
            compute_type="float16"
        )

    def transcribe(self, audio_path):
        segments, info = self.model.transcribe(audio_path)
        return segments, info
