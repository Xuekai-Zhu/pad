def solution():
    # Calculate the total number of cupcakes Jean bought
    total_cupcakes = 4 * 15  # Jean bought 4 packs of 15 cupcakes

    # Calculate the number of cupcakes needed to feed 100 children
    cupcakes_needed = 100

    # Calculate the number of packs of 10 cupcakes Jean needs to buy
    packs_of_10 = (cupcakes_needed - total_cupcakes) / 10
    result = math.ceil(packs_of_10)
    return result

print(solution())