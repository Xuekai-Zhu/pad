def solution():
    
    petals_per_ounce = 320
    petals_per_rose = 8
    roses_per_bush = 12
    ounces_per_bottle = 12
    bottles_needed = 20
    petals_needed = petals_per_ounce * ounces_per_bottle * bottles_needed
    roses_needed = petals_needed / petals_per_rose / roses_per_bush
    result = roses_needed
    return result

print(solution())