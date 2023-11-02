def solution():
    
    traveler_drinks = 32
    camel_drinks = 7 * traveler_drinks
    total_drinks = traveler_drinks + camel_drinks
    gallons = total_drinks / 128
    result = gallons
    return result

print(solution())