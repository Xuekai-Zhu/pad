def solution():
    """A building has 300 units. Half the units are residential and the other half are split evenly between offices and restaurants. How many restaurants are there in the building?"""
    total_units = 300
    residential_units = total_units / 2
    non_residential_units = total_units - residential_units
    restaurant_units = non_residential_units / 2
    result = restaurant_units
    return result

print(solution())