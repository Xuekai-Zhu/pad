def solution():
    """Ginger ended up working 8 hours outside in her garden. She kept a water bottle with her that held 2 cups of water. She drank a full bottle of every hour she was outside. She also poured an additional 5 bottles of water over the new plants she planted. How many cups of water did Ginger drink/use that day?"""
    hours_working = 8
    bottles_consumed = hours_working
    cups_per_bottle = 2
    total_cups_consumed = bottles_consumed * cups_per_bottle
    cups_used_for_plants = 5 * cups_per_bottle
    total_cups = total_cups_consumed + cups_used_for_plants
    result = total_cups
    return result

print(solution())