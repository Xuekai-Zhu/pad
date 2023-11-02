def solution():
    # Calculate the area of the house
    area_house = 20.5 * 10

    # Calculate the area of the porch
    area_porch = 6 * 4.5

    # Calculate the total area to be covered with shingles
    total_area = area_house + area_porch

    # Calculate the amount of shingles needed
    shingles_needed = total_area / 100  # Assuming 1 bundle of shingles covers 100 sq ft

    result = shingles_needed
    return result

print(solution())