def solution():
    total_cupcakes_needed = 144
    cherry_cupcakes = 36
    berry_cupcakes = 48

    # Calculate the number of cupcakes that Mary still needs to make
    cupcakes_left = total_cupcakes_needed - cherry_cupcakes - berry_cupcakes

    # Calculate the number of chocolate cupcakes
    chocolate_cupcakes = cupcakes_left // 2

    # Calculate the number of vanilla cupcakes
    vanilla_cupcakes = cupcakes_left // 2

    # If cupcakes_left is odd, add one more to either chocolate or vanilla cupcakes
    if cupcakes_left % 2 == 1:
        chocolate_cupcakes += 1

    result = (chocolate_cupcakes, vanilla_cupcakes)
    return result

print(solution())