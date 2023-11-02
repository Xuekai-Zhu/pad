def solution():
    num_avocados_needed = 3
    starting_avocados = 5
    sister_avocados = 4

    # Calculate the total number of avocados Georgie has after her sister buys more
    total_avocados = starting_avocados + sister_avocados

    # Calculate the maximum number of servings of guacamole Georgie can make
    max_servings = total_avocados // num_avocados_needed

    result = max_servings
    return result

print(solution())