def solution():
    """Jacob is making s'mores. Each s'more takes two graham crackers and one marshmallow. If Jacob has 48 graham crackers and 6 marshmallows, how many more marshmallows does he need to buy?"""
    # Calculate the maximum number of s'mores Jacob can make with the given ingredients
    max_smore = min(48 // 2, 6 // 1)

    # Calculate the remaining ingredients after making the maximum number of s'mores
    remaining_graham = 48 - max_smore * 2
    remaining_marshmallow = 6 - max_smore * 1

    # Calculate the number of additional marshmallows needed to make the same number of s'mores as graham crackers
    additional_marshmallow = 48 // 2 - max_smore

    result = additional_marshmallow
    return result

print(solution())