def solution():
    traveler_drink = 32  # The traveler drank 32 ounces of water
    camel_drink = 7 * traveler_drink  # The camel drank seven times as much as the traveler
    total_drink = traveler_drink + camel_drink  # Calculate the total amount of water they drank
    gallons = total_drink / 128  # Convert the total amount of water to gallons
    result = gallons
    return result

print(solution())