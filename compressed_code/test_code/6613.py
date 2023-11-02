def solution():
    
    gallons = 20
    containers = 80
    gallons_per_container = gallons / containers
    containers_drunk = 3.5
    gallons_drunk = containers_drunk * gallons_per_container
    pints_drunk = gallons_drunk * 8
    result = pints_drunk
    return result

print(solution())