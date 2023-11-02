def solution():
    num_children = 45
    num_adults = num_children * 3
    num_adults_wearing_blue = num_adults / 3

    # Calculate the number of adults who did not wear blue
    num_adults_not_wearing_blue = num_adults - num_adults_wearing_blue
    result = num_adults_not_wearing_blue
    return result

print(solution())