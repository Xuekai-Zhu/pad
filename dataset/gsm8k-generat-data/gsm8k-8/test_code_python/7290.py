def solution():
    # Define the number of units in the building
    total_units = 300

    # Calculate the number of residential units
    residential_units = total_units / 2

    # Calculate the number of non-residential units
    non_residential_units = total_units - residential_units

    # Divide the non-residential units evenly between offices and restaurants
    restaurant_units = non_residential_units / 2

    result = restaurant_units
    return result

print(solution())