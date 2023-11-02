def solution():
    starting_temp = 41
    boiling_temp = 212
    temp_increase_per_minute = 3
    pasta_cooking_time = 12
    pasta_mixing_time = pasta_cooking_time / 3

    # Calculate how long it takes to bring the water to a boil
    time_to_boil = (boiling_temp - starting_temp) / temp_increase_per_minute

    # Calculate the total cooking time for the pasta
    total_cooking_time = time_to_boil + pasta_cooking_time + pasta_mixing_time
    result = total_cooking_time
    return result

print(solution())