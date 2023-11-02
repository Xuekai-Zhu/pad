def solution():
    """Jason is making pasta. He fills the pot with 41 degree water. Each minute the temperature of the water increases by 3 degrees. Once the water reaches 212 degrees and is boiling, Jason needs to cook his pasta for 12 minutes. Then it will take him 1/3 that long to mix the pasta with the sauce and make a salad. How many minutes does it take Jason to cook dinner?"""
    # Calculate the time it takes to bring the water to boiling (212 degrees)
    initial_temp = 41
    boiling_temp = 212
    temp_increase_per_minute = 3
    time_to_boil = (boiling_temp - initial_temp) / temp_increase_per_minute

    # Calculate the total time it takes to cook the pasta and mix with sauce/salad
    pasta_cooking_time = 12
    mixing_time = pasta_cooking_time / 3

    # Calculate the total time it takes to cook dinner
    total_cooking_time = time_to_boil + pasta_cooking_time + mixing_time

    # Display the total cooking time
    result = total_cooking_time
    return result

print(solution())