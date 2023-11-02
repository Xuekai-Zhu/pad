def solution():
    """Jason is making pasta. He fills the pot with 41 degree water. Each minute the temperature of the water increases by 3 degrees. Once the water reaches 212 degrees and is boiling, Jason needs to cook his pasta for 12 minutes. Then it will take him 1/3 that long to mix the pasta with the sauce and make a salad. How many minutes does it take Jason to cook dinner?"""
    # Calculate the number of minutes it takes for the water to boil
    water_temp = 41
    boil_temp = 212
    degree_increase = 3
    minutes_to_boil = (boil_temp - water_temp) / degree_increase

    # Calculate the total cooking time
    pasta_cook_time = 12
    mix_time = pasta_cook_time / 3
    total_cook_time = minutes_to_boil + pasta_cook_time + mix_time

    # Return the result
    result = total_cook_time
    return result

print(solution())