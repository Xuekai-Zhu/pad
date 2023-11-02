def solution():
    cakes_monday = 6
    cakes_friday = 9
    cakes_saturday = cakes_monday * 3

    # Calculate the total number of cakes Leila ate last week
    total_cakes = cakes_monday + cakes_friday + cakes_saturday
    result = total_cakes
    return result

print(solution())