def solution():
    total_members = 120
    adult_percent = 0.4
    num_adults = total_members * adult_percent
    num_children = total_members - num_adults
    difference = num_children - num_adults
    result = difference
    return result

print(solution())