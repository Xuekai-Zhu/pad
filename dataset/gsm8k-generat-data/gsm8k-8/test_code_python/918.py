def solution():
    # Calculate area of house
    house_area = 20.5 * 10

    # Calculate area of porch
    porch_area = 6 * 4.5

    # Calculate total area to be shingled
    total_area = house_area + porch_area

    # Convert to square feet of shingles needed
    shingle_area = total_area * 2

    result = shingle_area
    return result

print(solution())