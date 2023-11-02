def solution():
    total_sodas = 12
    num_sisters = 2
    num_brothers = num_sisters * 2
    total_siblings = num_sisters + num_brothers
    sodas_per_sibling = total_sodas / total_siblings
    result = sodas_per_sibling
    return result

print(solution())