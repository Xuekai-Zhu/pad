def solution():
    # Calculate the number of restaurants in the building
    residential_units = 300 / 2  # half the units are residential
    non_residential_units = 300 / 2 # other half of units are non-residential
    restaurants = non_residential_units / 2 # non-residential units are split evenly between offices and restaurants
    result = restaurants
    return result

print(solution())