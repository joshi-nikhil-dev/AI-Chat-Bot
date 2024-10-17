from transformers import pipeline
import torch

class TextSummarizer:
    def __init__(self):
        """
        Initialize the TextSummarizer with a summarization pipeline.
        
        The pipeline uses the 'sshleifer/distilbart-cnn-12-6' model for summarization. 
        It will utilize a GPU if available; otherwise, it will fall back to CPU.
        """
        # Check if GPU is available, otherwise use CPU
        device: int = 0 if torch.cuda.is_available() else -1
        self.summarizer = pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6",  # Specify the summarization model
            device=device  # Use GPU if available
        )

    def summarize(self, text: str) -> str:
        """
        Summarize the provided text.

        Parameters:
        text (str): The input text to be summarized.

        Returns:
        str: The summarized text.
        """
        # Summarize the input text
        summary: list = self.summarizer(text, max_length=50, min_length=25, do_sample=False)
        return summary[0]['summary_text']
