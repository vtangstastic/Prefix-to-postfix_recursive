class PrefixToPostfixConverter:
    def __init__(self):
        # Initialize the set of operators
        self.operators = {'+', '-', '*', '/', '$'}

    def prefix_to_postfix(self, prefix):
        """
        Convert a prefix expression to postfix.
        
        Args:
            prefix (str): The prefix expression to be converted.

        Returns:
            str: The equivalent postfix expression.

        Errors:
            Print error: If the prefix expression is invalid.
        """

        def process_char(index):            
            # Check if the prefix expression only has one character
            if len(prefix) == 1 or prefix[index::] in self.operators:
                return "Invalid prefix expression", index

            # Base case
            if index >= len(prefix):
                # If we've reached the end of the expression, return an empty string and the index
                return '', index

            char = prefix[index]
            if char.isalpha():
                # If the character is an alphabet, return the character and move to the next index
                return char, index + 1
            elif char in self.operators:
                # If the character is an operator, recursively process the next two operands
                left_operand, next_index = process_char(index + 1)
                right_operand, next_index = process_char(next_index)
                # Concatenate the left operand, right operand, and operator to form postfix expression
                return left_operand + right_operand + char, next_index
            else:
                # If the character is not valid, return an error message and the current index
                return 'Invalid character in prefix expression', index

        # Start processing from the beginning of the prefix expression
        result, next_index = process_char(0)

        # Ensure all characters are processed
        if next_index != len(prefix):
            # If there are remaining characters after processing, return an error message
            return 'Invalid prefix expression'

        return result