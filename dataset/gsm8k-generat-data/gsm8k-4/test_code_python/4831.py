def solution():
    """Joyce moved to the countryside because she needed more farmland to grow her vegetables. Her new property is 10 times larger than her previous property, but her new land has a 1-acre pond on it where she cannot grow vegetables. If her previous property was 2 acres, how many acres of land does she now own that are suitable for growing vegetables?"""
    # Define the size of Joyce's previous property and the size of her new property
    previous_property_size = 2
    new_property_size = previous_property_size * 10

    # Subtract the size of the pond from the size of the new property to find the size of land suitable for growing vegetables
    vegetable_land_size = new_property_size - 1

    # return the result
    result = vegetable_land_size
    return result

print(solution())