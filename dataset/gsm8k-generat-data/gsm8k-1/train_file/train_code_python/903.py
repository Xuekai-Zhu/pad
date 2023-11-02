def solution():
    """Audrey's key lime pie calls for 1/4 cup of key lime juice but she likes to double this amount to make it extra tart. Each key lime yields 1 tablespoon of juice. There are 16 tablespoons in 1 cup. How many key limes does Audrey need?"""
    juice_per_pie = 1/4 * 2  # double the amount for extra tartness
    tablespoons_per_cup = 16
    juice_per_cup = tablespoons_per_cup / 4  # 4 tablespoons = 1/4 cup
    key_limes_per_tablespoon = 1
    key_limes_needed = juice_per_pie * juice_per_cup / key_limes_per_tablespoon
    result = key_limes_needed
    return result

print(solution())