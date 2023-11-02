def solution():
    # Calculate the total number of cupcakes baked
    total_cupcakes = 4 * 20

    # Calculate the number of cupcakes sold
    cupcakes_sold = int(total_cupcakes * 3/5)

    # Calculate the earnings from the cupcakes sold
    earnings = cupcakes_sold * 2

    result = earnings
    return result

print(solution())