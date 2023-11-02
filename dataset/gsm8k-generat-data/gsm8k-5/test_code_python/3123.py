def solution():
    water_bottle_capacity = 12  # Madeline's water bottle can hold 12 ounces of water
    refills = 7  # Madeline refills her water bottle 7 times in a day
    total_water = water_bottle_capacity * refills  # Madeline drinks this much water from her bottle
    remaining_water = 100 - total_water  # Madeline's goal is to drink 100 ounces of water in a day, so she needs to drink this much more

    result = remaining_water
    return result

print(solution())