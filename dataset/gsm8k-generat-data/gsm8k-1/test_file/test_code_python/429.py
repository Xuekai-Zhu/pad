def solution():
    """15 gallons of gas were equally divided into 5 different containers. Josey needed 1/4 of a container to run her lawnmower. How many pints of gasoline did Josey need?"""
    total_gallons = 15
    containers = 5
    gallons_per_container = total_gallons / containers
    fraction_needed = 1/4
    gallons_needed = gallons_per_container * fraction_needed
    pints_needed = gallons_needed * 8
    result = pints_needed
    return result

print(solution())