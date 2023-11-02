def solution():
    num_roofs = 3
    side1_length = 20
    side2_length = 40
    shingles_per_sqft = 8

    # Calculate the area of one side of the roof
    area_per_side = side1_length * side2_length

    # Calculate the total area of both sides of one roof
    total_area_per_roof = area_per_side * 2

    # Calculate the total area of both sides of all three roofs
    total_area_all_roofs = total_area_per_roof * num_roofs

    # Calculate the total number of shingles needed
    total_shingles = total_area_all_roofs * shingles_per_sqft
    result = total_shingles
    return result

print(solution())