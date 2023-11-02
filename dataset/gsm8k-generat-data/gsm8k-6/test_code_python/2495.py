def solution():
    # Calculate the total amount of water they drank
    traveler_drink = 32  # ounces of water the traveler drank
    camel_drink = 7 * traveler_drink  # ounces of water the camel drank
    total_drink = traveler_drink + camel_drink  # total ounces of water they drank
    total_gallons = total_drink / 128  # convert ounces to gallons
    result = total_gallons
    return result

print(solution())