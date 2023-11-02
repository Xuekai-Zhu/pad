def solution():
    """A building has 300 units. Half the units are residential and the other half are split evenly between offices and restaurants. How many restaurants are there in the building?"""
    # Define the total number of units and the number of residential units
    total_units = 300
    residential_units = total_units / 2

    # Calculate the number of non-residential units
    non_residential_units = total_units - residential_units

    # Calculate the number of units that are split evenly between offices and restaurants
    non_residential_split = non_residential_units / 2

    # Calculate the number of restaurant units
    restaurant_units = non_residential_split

    # Return the result
    result = restaurant_units
    return result

print(solution())