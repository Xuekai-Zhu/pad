def solution():
    # Codger has 3 feet and needs 3 shoes per foot, so he currently has 9 shoes
    current_shoes = 9

    # 5 complete 3-piece sets of shoes would require 15 shoes total
    total_shoes_needed = 15

    # Each pair of shoes has 2 shoes, so Codger needs to buy 3 pairs of shoes
    pairs_of_shoes_needed = (total_shoes_needed - current_shoes) / 2

    result = pairs_of_shoes_needed
    return result

print(solution())