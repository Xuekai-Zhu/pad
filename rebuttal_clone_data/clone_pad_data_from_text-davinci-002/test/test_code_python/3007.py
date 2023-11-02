def solution():
    total_children = 45
    total_adults = total_children / 3
    total_blue_adults = total_adults / 3
    total_non_blue_adults = total_adults - total_blue_adults
    result = total_non_blue_adults
    return result

print(solution())