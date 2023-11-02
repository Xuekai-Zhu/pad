def solution():
    # Calculate the total number of tomatoes harvested
    total_tomatoes = 18 * 7

    # Calculate the number of tomatoes to be dried
    tomatoes_dried = total_tomatoes / 2

    # Calculate the number of remaining tomatoes
    tomatoes_remaining = total_tomatoes - tomatoes_dried

    # Calculate the number of tomatoes to be turned into marinara sauce
    tomatoes_sauce = tomatoes_remaining / 3

    # Calculate the final number of tomatoes left
    tomatoes_left = tomatoes_remaining - tomatoes_sauce
    result = tomatoes_left
    return result

print(solution())