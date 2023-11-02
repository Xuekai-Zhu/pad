def solution():
    # Calculate the total weight of groceries Mary has bought
    total_weight = 4 + 6 + (2 * 4)  # twice the amount of green beans (4)

    # Calculate how much more weight Mary can fit in the bag
    remaining_weight = 20 - total_weight
    result = remaining_weight
    return result

print(solution())