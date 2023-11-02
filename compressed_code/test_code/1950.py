def solution():
    
    traveler_drink = 32
    camel_drink = 7 * traveler_drink
    total_drink = traveler_drink + camel_drink
    gallons = total_drink / 128
    result = gallons
    return result

print(solution())