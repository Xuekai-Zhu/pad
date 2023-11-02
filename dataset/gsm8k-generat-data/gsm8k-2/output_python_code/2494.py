def solution():
    """A thirsty traveler found an oasis in the desert. He drank 32 ounces of water. His camel drank seven times as much as he did. There are 128 ounces in a gallon. How many gallons of water did they drink altogether?"""
    traveler_drink = 32
    camel_drink = 7 * traveler_drink
    total_drink = traveler_drink + camel_drink
    gallons = total_drink / 128
    result = gallons
    return result

print(solution())