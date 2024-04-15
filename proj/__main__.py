import argparse  # Import the argparse module for command-line argument parsing
from .prefix_to_postfix import PrefixToPostfixConverter  # Import the PrefixToPostfixConverter class from prefix_to_postfix module

def main():
    # Create an ArgumentParser object for parsing command-line arguments
    arg_parser = argparse.ArgumentParser()
    # Add arguments for input and output file paths
    arg_parser.add_argument("input_file", type=str, help="Input File Pathname")
    arg_parser.add_argument("output_file", type=str, help="Output File Pathname")
    # Parse the command-line arguments
    args = arg_parser.parse_args()

    # Extract input and output file paths from the parsed arguments
    input_file_path = args.input_file
    output_file_path = args.output_file

    try:
        # Open the input and output files
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
            # Create an instance of PrefixToPostfixConverter
            converter = PrefixToPostfixConverter()
            # Iterate through each line in the input file
            for line in input_file:
                # Strip newline characters and whitespace from the line to get the prefix expression
                prefix_expression = line.strip()
                
                # Check if the line is empty or contains only spaces
                if prefix_expression.strip() == "":
                    output_file.write("Blank: There is no input\n")
                    continue
                
                # Convert the prefix expression to postfix using the PrefixToPostfixConverter instance
                postfix_expression = converter.prefix_to_postfix(prefix_expression)
                # Write the prefix and postfix expressions to the output file
                output_file.write(f"Prefix expression: {prefix_expression}\n")
                output_file.write(f"Postfix expression: {postfix_expression}\n")
    except FileNotFoundError:
        # Handle the FileNotFoundError exception if the input file is not found
        print(f"Error: Input file '{input_file_path}' not found.")
    except Exception as e:
        # Handle any other exceptions that may occur during execution
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # If the script is executed directly, call the main function
    main()
