def solution():
    """Mary wants 144 cupcakes for her party. Mary has already made 36 cherry cupcakes, and 48 berry cupcakes. Mary wants to make an even number of chocolate and vanilla cupcakes for the rest. How much of each should she make?"""
    # Define the total number of cupcakes Mary needs
    total_cupcakes = 144

    # Define the number of cherry and berry cupcakes Mary already made
    cherry_cupcakes = 36
    berry_cupcakes = 48

    # Calculate the number of cupcakes Mary still needs to make
    remaining_cupcakes = total_cupcakes - cherry_cupcakes - berry_cupcakes

    # Calculate the number of chocolate and vanilla cupcakes Mary should make
    chocolate_cupcakes = remaining_cupcakes // 2
    vanilla_cupcakes = remaining_cupcakes // 2

    result = (chocolate_cupcakes, vanilla_cupcakes)
    return result

print(solution())