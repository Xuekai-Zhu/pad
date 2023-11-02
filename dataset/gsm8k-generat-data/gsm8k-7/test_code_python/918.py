def solution():
    # Calculate the area of the house
    house_area = 20.5 * 10

    # Calculate the area of the porch
    porch_area = 6 * 4.5

    # Calculate the total area that needs to be roofed
    total_area = house_area + porch_area

    # Calculate the amount of shingles needed to roof the total area
    # Assume that one bundle of shingles covers 33.33 square feet
    num_shingle_bundles = total_area / 33.33

    # Round up to the nearest whole number of bundles
    num_shingle_bundles = math.ceil(num_shingle_bundles)

    # Calculate the total square footage of shingles needed
    total_shingle_area = num_shingle_bundles * 33.33
    result = total_shingle_area
    return result

print(solution())