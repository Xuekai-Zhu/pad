def solution():
    # Define the time John spends in the first country
    country1_time = 2

    # Define the time John spends in the second and third countries
    country2_time = country1_time * 2
    country3_time = country1_time * 2

    # Calculate the total time John spends on the trip
    total_time = country1_time + country2_time + country3_time
    result = total_time
    return result

print(solution())