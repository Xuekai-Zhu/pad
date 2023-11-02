def solution():
    
    servings_per_pie = 8
    pies = 3
    guests = 12
    apples_per_serving = 1.5
    total_apples = servings_per_pie * pies * apples_per_serving
    apples_per_guest = total_apples / guests
    result = apples_per_guest
    return result

print(solution())