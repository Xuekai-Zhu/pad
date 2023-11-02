def solution():
    # Calculate the total number of cupcakes Jean has
    total_cupcakes = 4 * 15

    # Calculate the number of cupcakes she needs to give out
    cupcakes_to_give = 100

    # Calculate the remaining cupcakes she needs to buy
    remaining_cupcakes = cupcakes_to_give - total_cupcakes

    # Calculate the number of packs of 10 cupcakes she needs to buy
    packs_of_10 = remaining_cupcakes // 10
    if remaining_cupcakes % 10 != 0:
        packs_of_10 += 1

    result = packs_of_10
    return result

print(solution())