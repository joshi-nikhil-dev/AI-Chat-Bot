class MultiplicationTool:
    def multiply_numbers(self, numbers):
        """
        Multiply a list of numbers and return the product.

        Parameters:
        numbers (list): A list of numbers to multiply.

        Returns:
        int: The product of the numbers.
        """
        product = 1
        for number in numbers:
            product *= number
        return product
