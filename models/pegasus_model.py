from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch

class PegasusModelWrapper:
    def __init__(self, model_name="google/pegasus-xsum"):
        self.tokenizer = PegasusTokenizer.from_pretrained(model_name)
        self.model = PegasusForConditionalGeneration.from_pretrained(model_name)
        if torch.cuda.is_available():
            self.model = self.model.to("cuda")

    def summarize(self, text, max_length=150, min_length=30):
        tokens = self.tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
        if torch.cuda.is_available():
            tokens = {k: v.to("cuda") for k, v in tokens.items()}
        summary_ids = self.model.generate(
            tokens["input_ids"],
            max_length=max_length,
            min_length=min_length,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
