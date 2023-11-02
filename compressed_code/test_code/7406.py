def solution():
    
    apples_per_pie = 8
    pies_to_bake = 10
    apples_already_have = 50
    total_apples_needed = apples_per_pie * pies_to_bake - apples_already_have
    result = total_apples_needed
    return result

print(solution())