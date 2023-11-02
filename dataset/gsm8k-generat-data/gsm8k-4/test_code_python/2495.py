def solution():
    """A thirsty traveler found an oasis in the desert. He drank 32 ounces of water. His camel drank seven times as much as he did. There are 128 ounces in a gallon. How many gallons of water did they drink altogether?"""
    # Define the amount of water the traveler drank and the amount his camel drank
    traveler_drink = 32
    camel_drink = 7 * traveler_drink

    # Calculate the total amount of water they drank
    total_drink = traveler_drink + camel_drink

    # Convert the total amount of water to gallons
    total_gallons = total_drink / 128

    # Return the result
    result = total_gallons
    return result

print(solution())