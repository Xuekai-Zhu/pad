def solution():
    
    avocados_needed = 3
    avocados_owned = 5
    additional_avocados = 4
    total_avocados = avocados_owned + additional_avocados
    servings_possible = total_avocados // avocados_needed
    result = servings_possible
    return result

print(solution())