from models.pegasus_model import PegasusModelWrapper
import re

class SummarizationService:
    def __init__(self):
        self.pegasus = PegasusModelWrapper()

    def summarize_transcript(self, transcript):
        cleaned_text = re.sub(r'\[\d+\.\d+s -> \d+\.\d+s\]', '', transcript)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text.strip())
        summary = self.pegasus.summarize(cleaned_text)
        return summary
