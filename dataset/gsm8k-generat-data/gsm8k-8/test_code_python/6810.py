def solution():
    # Calculate the total number of cakes baked
    total_cakes_baked = 20 * 9

    # Calculate the number of cakes sold
    cakes_sold = total_cakes_baked / 2

    # Calculate the number of cakes left with Brenda
    cakes_left = total_cakes_baked - cakes_sold

    result = cakes_left
    return result

print(solution())