def solution():
    """A traveler and his camel drink water from an oasis in the desert. The traveler drinks 32 ounces and the camel drinks seven times as much. There are 128 ounces in a gallon. How many gallons of water did they drink altogether?"""
    traveler_drinks = 32
    camel_drinks = 7 * traveler_drinks
    total_drinks = traveler_drinks + camel_drinks
    gallons = total_drinks / 128
    result = gallons
    return result

print(solution())