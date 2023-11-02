def solution():
    
    total_members = 120
    adult_percentage = 0.4
    num_adults = int(total_members * adult_percentage)
    num_children = total_members - num_adults
    diff_children_adults = num_children - num_adults
    result = diff_children_adults
    return result

print(solution())