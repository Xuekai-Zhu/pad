def solution():
    """The city of Richmond has 1000 more people than Victoria. Victoria has 4 times as many people as Beacon. If Richmond has 3000 people, how many people are there in Beacon?"""
    # Define the number of people in Richmond and Victoria
    richmond_population = 3000
    victoria_population = richmond_population - 1000

    # Calculate the number of people in Beacon
    beacon_population = victoria_population / 4

    result = beacon_population
    return result

print(solution())