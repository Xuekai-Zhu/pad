def solution():
    # Calculate the amount of ounces Amber can get if she buys candy
    candy_ounces = 7 // 1 * 12  # each bag of candy costs $1 and contains 12 ounces

    # Calculate the amount of ounces Amber can get if she buys chips
    chips_ounces = (7 // 1.4) * 17  # each bag of chips costs $1.40 and contains 17 ounces

    # Return the maximum ounces Amber can get
    result = max(candy_ounces, chips_ounces)
    return result

print(solution())