def solution():
    total_cupcakes = 96
    cupcakes_given = 24
    cupcakes_needed = total_cupcakes - cupcakes_given
    cupcakes_per_day = cupcakes_needed / 2
    result = cupcakes_per_day
    return result

print(solution())