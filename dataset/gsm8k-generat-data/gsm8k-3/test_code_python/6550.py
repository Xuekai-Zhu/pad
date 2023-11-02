def solution():
    """In a car dealership with 600 cars, 60% of the cars are hybrids, and 40% of the hybrids contain only one headlight. How many of the hybrids have full headlights?"""
    # Define the number of cars in the dealership
    total_cars = 600

    # Calculate the number of hybrids
    hybrids = total_cars * 0.6

    # Calculate the number of hybrids with one headlight
    hybrids_one_headlight = hybrids * 0.4

    # Calculate the number of hybrids with two headlights (i.e. full headlights)
    hybrids_full_headlights = hybrids - hybrids_one_headlight

    # Display the number of hybrids with full headlights
    result = hybrids_full_headlights
    return result

print(solution())