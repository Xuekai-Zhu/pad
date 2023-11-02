def solution():
    # Calculate the area of one side of the roof
    side_area = 20 * 40

    # Calculate the total area of one roof
    roof_area = 2 * side_area

    # Calculate the total area of all 3 roofs
    total_roof_area = roof_area * 3

    # Calculate the total number of shingles needed
    shingles_needed = total_roof_area * 8

    result = shingles_needed
    return result

print(solution())