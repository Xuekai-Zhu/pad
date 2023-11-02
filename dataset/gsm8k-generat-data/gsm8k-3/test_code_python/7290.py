def solution():
    """A building has 300 units. Half the units are residential and the other half are split evenly between offices and restaurants. How many restaurants are there in the building?"""
    # Define the total number of units and the fraction that are restaurants
    TOTAL_UNITS = 300
    RESTAURANT_FRACTION = 0.25

    # Calculate the number of restaurant units
    restaurant_units = TOTAL_UNITS * RESTAURANT_FRACTION

    # Display the number of restaurant units
    result = restaurant_units
    return result

print(solution())