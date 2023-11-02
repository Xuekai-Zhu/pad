def solution():
    """Ginger ended up working 8 hours outside in her garden. She kept a water bottle with her that held 2 cups of water. She drank a full bottle of every hour she was outside. She also poured an additional 5 bottles of water over the new plants she planted. How many cups of water did Ginger drink/use that day?"""
    hours_working_outside = 8
    water_bottle_size = 2
    water_bottles_consumed = hours_working_outside
    water_poured_on_plants = 5 * water_bottle_size
    total_water_used = (water_bottles_consumed + water_poured_on_plants) * water_bottle_size
    result = total_water_used
    return result

print(solution())