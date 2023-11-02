def solution():
    
    num_adults = 2
    num_children = 4
    total_cookies = 120
    adult_share = total_cookies / 3
    child_share = (total_cookies - adult_share) / num_children
    result = child_share
    return result

print(solution())