def solution():
    # Calculate the number of green shoes
    green_shoes = (1250 - 540) / 2  # the rest of the shoes are either green or purple and their numbers are equal
    purple_shoes = green_shoes  # the number of green shoes is equal to the number of purple shoes
    result = purple_shoes
    return result

print(solution())