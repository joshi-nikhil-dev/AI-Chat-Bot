from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class TextFunifier:
    def __init__(self) -> None:
        """
        Initialize the DialoGPT-large model and tokenizer for funifying text.
        
        The model is loaded onto the GPU if available; otherwise, it defaults to the CPU.
        """
        self.model_name: str = "microsoft/DialoGPT-medium"  # Using DialoGPT-medium
        self.tokenizer: AutoTokenizer = AutoTokenizer.from_pretrained(self.model_name)
        
        # Load model and move to GPU if available
        self.device: torch.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model: AutoModelForCausalLM = AutoModelForCausalLM.from_pretrained(self.model_name).to(self.device)

    def funify(self, text: str) -> str:
        """
        Funify the input text using DialoGPT.

        Parameters:
        text (str): The input text to make funnier.

        Returns:
        str: The funified text.
        """
        # Tokenize the input text
        inputs: torch.Tensor = self.tokenizer.encode(text + self.tokenizer.eos_token, return_tensors="pt").to(self.device)

        # Generate a response
        outputs: torch.Tensor = self.model.generate(inputs, max_length=100, num_return_sequences=1, do_sample=True, temperature=0.9)

        # Decode the response
        funified_text: str = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return funified_text
