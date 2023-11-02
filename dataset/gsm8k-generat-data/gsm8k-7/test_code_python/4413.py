def solution():
    num_sisters = 2
    num_brothers = num_sisters * 2
    total_siblings = num_sisters + num_brothers
    sodas_per_sibling = 12 // total_siblings
    result = sodas_per_sibling
    return result

print(solution())