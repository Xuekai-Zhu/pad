def solution():
    cakes_on_monday = 6
    cakes_on_friday = 9
    cakes_on_saturday = cakes_on_monday * 3

    # Calculate the total number of cakes Leila ate
    total_cakes = cakes_on_monday + cakes_on_friday + cakes_on_saturday
    result = total_cakes
    return result

print(solution())