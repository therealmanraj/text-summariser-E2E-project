from textSummarizer.logging import logger
from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        
    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}
        
        pipeline_instance = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)
        print("Dialogue:", text)
        
        output = pipeline_instance(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:", output)
        
        return output
