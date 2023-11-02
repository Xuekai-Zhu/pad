def solution():
    soap = 3
    water = 1
    container_capacity = 40
    cups_to_ounces = 8
    ounces_of_water = cups_to_ounces * water
    ounces_of_soap = soap * water
    capacity_remaining = container_capacity - ounces_of_water
    tablespoons_of_soap = capacity_remaining / ounces_of_soap
    result = tablespoons_of_soap
    
    return result

print(solution())