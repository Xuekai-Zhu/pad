def solution():
    """Mary wants 144 cupcakes for her party. Mary has already made 36 cherry cupcakes, and 48 berry cupcakes. Mary wants to make an even number of chocolate and vanilla cupcakes for the rest. How much of each should she make?"""
    # Define the total number of cupcakes needed
    total_cupcakes = 144

    # Subtract the number of cherry and berry cupcakes from the total
    remaining_cupcakes = total_cupcakes - 36 - 48

    # Calculate the number of chocolate and vanilla cupcakes needed
    chocolate_cupcakes = remaining_cupcakes / 2
    vanilla_cupcakes = remaining_cupcakes / 2

    # Check if the number of cupcakes is odd
    if remaining_cupcakes % 2 == 1:
        # If odd, make one more vanilla cupcake
        vanilla_cupcakes += 1

    # Display the number of chocolate and vanilla cupcakes needed
    result = (chocolate_cupcakes, vanilla_cupcakes)
    return result

print(solution())