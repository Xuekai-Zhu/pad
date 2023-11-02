def solution():
    """Jason is making pasta. He fills the pot with 41 degree water. Each minute the temperature of the water increases by 3 degrees. Once the water reaches 212 degrees and is boiling, Jason needs to cook his pasta for 12 minutes. Then it will take him 1/3 that long to mix the pasta with the sauce and make a salad. How many minutes does it take Jason to cook dinner?"""
    initial_temp = 41
    boiling_temp = 212
    temp_increase_per_minute = 3
    time_to_boil = (boiling_temp - initial_temp) / temp_increase_per_minute
    time_to_cook_pasta = 12
    time_to_mix_and_make_salad = time_to_cook_pasta / 3
    total_time = time_to_boil + time_to_cook_pasta + time_to_mix_and_make_salad
    result = total_time
    return result

print(solution())