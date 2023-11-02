def solution():
    """In a car dealership with 600 cars, 60% of the cars are hybrids, and 40% of the hybrids contain only one headlight. How many of the hybrids have full headlights?"""
    # Define the total number of cars and the percentage of hybrids
    total_cars = 600
    hybrid_percentage = 0.6

    # Calculate the number of hybrid cars and cars with only one headlight
    hybrid_cars = total_cars * hybrid_percentage
    one_headlight = hybrid_cars * 0.4

    # Calculate the number of hybrid cars with full headlights
    full_headlights = hybrid_cars - one_headlight

    # return the result
    result = full_headlights
    return result

print(solution())