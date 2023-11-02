def solution():
    total_units = 300  # The building has 300 units
    residential_units = total_units // 2  # Half the units are residential
    non_residential_units = total_units - residential_units  # The other half are non-residential
    restaurants = non_residential_units // 2  # The non-residential units are split evenly between offices and restaurants

    result = restaurants
    return result

print(solution())