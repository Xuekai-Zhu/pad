def solution():
    
    meat_weight = 10 * 16  
    num_links = 40
    eaten_links = 12
    remaining_links = num_links - eaten_links
    remaining_meat_weight = meat_weight / num_links * remaining_links
    result = remaining_meat_weight
    return result

print(solution())