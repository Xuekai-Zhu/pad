def solution():
    """Joyce moved to the countryside because she needed more farmland to grow her vegetables. Her new property is 10 times larger than her previous property, but her new land has a 1-acre pond on it where she cannot grow vegetables. If her previous property was 2 acres, how many acres of land does she now own that are suitable for growing vegetables?"""
    previous_property = 2
    new_property = previous_property * 10
    suitable_land = new_property - 1
    result = suitable_land
    return result

print(solution())