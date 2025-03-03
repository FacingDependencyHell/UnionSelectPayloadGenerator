from itertools import combinations

def generate_payloads(num_positions, substitute_char, max_substitutions):
    payloads = []
    
    # Fixed mode: Replace exactly `max_substitutions` NULLs with the substitution character
    if max_substitutions > num_positions:
        print("Error: Number of substitutions cannot exceed the number of positions.")
        return payloads
    
    # Generate all combinations of positions to substitute
    for positions in combinations(range(num_positions), max_substitutions):
        payload = ['NULL'] * num_positions
        for pos in positions:
            payload[pos] = f"'{substitute_char}'"
        payloads.append(','.join(payload))
    
    return payloads

def main():
    # User inputs
    num_positions = int(input("How many positions: "))
    substitute_char = input("Character(s) to substitute: ")
    max_substitutions = int(input("How many substitutions: "))
    
    # Generate payloads
    payloads = generate_payloads(num_positions, substitute_char, max_substitutions)
    
    # Output the generated payloads
    print("\nGenerated Payloads:")
    for payload in payloads:
        print(payload)

if __name__ == "__main__":
    main()

