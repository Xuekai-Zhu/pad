def solution():
    
    apples_per_pie = 8
    total_pies = 10
    harvested_apples = 50
    total_apples_needed = apples_per_pie * total_pies
    remaining_apples_needed = total_apples_needed - harvested_apples
    result = remaining_apples_needed
    return result

print(solution())