def solution():
    """Jason is making pasta. He fills the pot with 41 degree water. Each minute the temperature of the water increases by 3 degrees. Once the water reaches 212 degrees and is boiling, Jason needs to cook his pasta for 12 minutes. Then it will take him 1/3 that long to mix the pasta with the sauce and make a salad. How many minutes does it take Jason to cook dinner?"""
    water_temp = 41
    boil_temp = 212
    rate_of_increase = 3
    time_to_boil = (boil_temp - water_temp) / rate_of_increase
    pasta_cook_time = 12
    mix_time = pasta_cook_time / 3
    total_time = time_to_boil + pasta_cook_time + mix_time
    result = total_time
    return result

print(solution())