def solution():
    # Calculate the remaining number of cupcakes that Mary needs to make
    remaining_cupcakes = 144 - 36 - 48  # Mary has already made 36 cherry cupcakes and 48 berry cupcakes

    # Make an even number of chocolate and vanilla cupcakes for the remaining cupcakes
    chocolate_cupcakes = remaining_cupcakes // 2
    vanilla_cupcakes = remaining_cupcakes // 2

    # If the remaining number of cupcakes is odd, make one more vanilla cupcake
    if remaining_cupcakes % 2 == 1:
        vanilla_cupcakes += 1

    # Return the number of chocolate and vanilla cupcakes that Mary should make
    result = (chocolate_cupcakes, vanilla_cupcakes)
    return result

print(solution())