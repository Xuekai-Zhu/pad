def solution():
    friday_magazines = 8
    saturday_magazines = 12
    sunday_magazines = friday_magazines * 4
    chewed_magazines = 4

    # Calculate the total number of magazines Alexandra bought
    total_magazines = friday_magazines + saturday_magazines + sunday_magazines - chewed_magazines

    result = total_magazines
    return result

print(solution())