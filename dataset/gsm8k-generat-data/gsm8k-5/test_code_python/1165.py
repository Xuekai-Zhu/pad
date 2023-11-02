def solution():
    # Calculate the area of one side of the roof
    roof_area = 20 * 40

    # Calculate the area of both sides of the roof
    total_roof_area = 2 * roof_area

    # Calculate the total area of all three roofs
    total_area = 3 * total_roof_area

    # Calculate the total number of shingles needed
    shingles_per_square_foot = 8  # 8 shingles per square foot
    total_shingles = shingles_per_square_foot * total_area

    result = total_shingles
    return result

print(solution())