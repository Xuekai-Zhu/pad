def solution():
    number_of_sisters = 2
    number_of_brothers = number_of_sisters * 2
    total_siblings = number_of_sisters + number_of_brothers
    sodas_per_sibling = 12 / total_siblings
    result = sodas_per_sibling
    return result

print(solution())