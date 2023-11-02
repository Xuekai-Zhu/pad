def solution():
    
    total_members = 120
    percent_adults = 40
    num_adults = total_members * (percent_adults / 100)
    num_children = total_members - num_adults
    difference = num_children - num_adults
    result = difference
    return result

print(solution())