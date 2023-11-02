def solution():
    rings_first_tree = 70
    rings_second_tree = 40
    total_rings = rings_first_tree + rings_second_tree
    age_first_tree = total_rings / 2
    age_second_tree = total_rings / 4
    difference = age_first_tree - age_second_tree
    result = difference
    
    return result

print(solution())