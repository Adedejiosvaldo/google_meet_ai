from models.whisper_model import WhisperModelWrapper
from utils.text_correction import correct_text

class TranscriptionService:
    def __init__(self):
        self.whisper = WhisperModelWrapper()

    def transcribe_audio(self, audio_path):
        segments, info = self.whisper.transcribe(audio_path)
        transcript_lines = []
        for segment in segments:
            corrected = correct_text(segment.text)
            line = f"[{segment.start:.2f}s -> {segment.end:.2f}s] {corrected}"
            transcript_lines.append(line)
        language_info = f"Detected language: {info.language} (probability: {info.language_probability:.2f})"
        return transcript_lines, language_info
