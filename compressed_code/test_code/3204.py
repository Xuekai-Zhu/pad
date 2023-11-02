def solution():
    
    servings_per_pie = 8
    apples_per_serving = 1.5
    num_pies = 3
    num_guests = 12
    total_servings = servings_per_pie * num_pies
    total_apples = total_servings * apples_per_serving
    apples_per_guest = total_apples / num_guests
    result = round(apples_per_guest, 2)
    return result

print(solution())