def solution():
    
    total_children = 180
    boys_ratio = 5
    girls_ratio = 7
    total_ratio = boys_ratio + girls_ratio
    boys_count = total_children * (boys_ratio / total_ratio)
    boys_share = 3900 / boys_count
    result = boys_share
    return result

print(solution())