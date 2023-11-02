def solution():
    starting_temperature = 41  # The starting temperature of the water
    boiling_temperature = 212  # The temperature at which the water boils
    temperature_increase_per_minute = 3  # The temperature increases by 3 degrees per minute
    time_to_boil = (boiling_temperature - starting_temperature) / temperature_increase_per_minute  # The time it takes for the water to boil
    time_to_cook_pasta = 12  # The time it takes to cook the pasta
    time_to_mix_and_make_salad = time_to_cook_pasta / 3  # It takes 1/3 the time to mix the pasta with the sauce and make a salad

    # Calculate the total time it takes Jason to cook dinner
    total_time = time_to_boil + time_to_cook_pasta + time_to_mix_and_make_salad
    result = total_time
    return result

print(solution())