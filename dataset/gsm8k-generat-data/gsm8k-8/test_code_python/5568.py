def solution():
    # Define the total number of cupcakes needed
    total_cupcakes = 144

    # Define the number of cherry and berry cupcakes already made
    cherry_cupcakes = 36
    berry_cupcakes = 48

    # Calculate the number of cupcakes still needed
    cupcakes_needed = total_cupcakes - cherry_cupcakes - berry_cupcakes

    # Calculate the number of chocolate and vanilla cupcakes needed
    chocolate_cupcakes = cupcakes_needed // 2
    vanilla_cupcakes = cupcakes_needed - chocolate_cupcakes

    result = (chocolate_cupcakes, vanilla_cupcakes)
    return result

print(solution())