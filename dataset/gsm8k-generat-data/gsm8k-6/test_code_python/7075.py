def solution():
    # Calculate the total weight of sugar in the packs
    total_weight = 12 * 250  # each pack weighs 250 grams
    remaining_weight = total_weight - (12 * 20)  # each pack has 20 grams of sugar left
    start_weight = remaining_weight + (12 * 20)  # add the amount of sugar left in each pack
    result = start_weight
    return result

print(solution())