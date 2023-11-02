def solution():
    # Number of graham crackers and marshmallows required for one s'more
    crackers_per_smore = 2
    marshmallows_per_smore = 1

    # Calculate the maximum number of s'mores Jacob can make with given ingredients
    max_smore_count = min(48 // crackers_per_smore, 6 // marshmallows_per_smore)

    # Calculate the number of marshmallows Jacob needs to buy to make more s'mores
    remaining_marshmallows = (max_smore_count * marshmallows_per_smore) - 6

    result = remaining_marshmallows
    return result

print(solution())