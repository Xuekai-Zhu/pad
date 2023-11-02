def solution():
    # Calculate the total number of peanuts Uncle Lou has
    total_peanuts = 4 * 30  # each bag contains 30 peanuts, and he has four bags

    # Calculate the amount of time it takes to eat each peanut, in minutes
    time_per_peanut = 2 * 60 / total_peanuts  # he has 2 hours for the flight, which is 120 minutes

    result = time_per_peanut
    return result

print(solution())