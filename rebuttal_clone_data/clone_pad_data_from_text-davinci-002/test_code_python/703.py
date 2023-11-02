def solution():
    avocados_needed = 3
    avocados_had = 5
    avocados_bought = 4
    avocados_total = avocados_needed + avocados_had + avocados_bought
    servings = avocados_total / avocados_needed
    result = servings
    return result

print(solution())