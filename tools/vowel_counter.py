class VowelCounter:
    def count_vowels(self, text: str) -> int:
        """
        Count the number of vowels in the given text.

        Parameters:
        text (str): The input text in which to count vowels.

        Returns:
        int: The count of vowels in the input text.
        """
        vowels = 'aeiouAEIOU'
        return sum(1 for char in text if char in vowels)
