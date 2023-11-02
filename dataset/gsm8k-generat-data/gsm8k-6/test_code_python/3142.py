def solution():
    # Calculate the liters of oil in the large tanker after pouring 3/4 of the oil from the 4000-liter tank
    large_tanker = (3/4) * 4000 + 3000  # liters of oil in the large tanker

    # Calculate the capacity of the large tanker when it is half-full
    half_tanker = 1/2 * 20000  # liters of oil needed to make the large tanker half-full

    # Calculate the liters of oil needed to fill the large tanker half-full
    oil_needed = half_tanker - large_tanker

    result = oil_needed
    return result

print(solution())