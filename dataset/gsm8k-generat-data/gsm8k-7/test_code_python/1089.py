def solution():
    starting_cans = 12
    sprinkles_used = ((starting_cans / 2) - 3) * 3  # 3 for hair, clothing, and pets
    remaining_cans = starting_cans - sprinkles_used
    result = remaining_cans
    return result

print(solution())