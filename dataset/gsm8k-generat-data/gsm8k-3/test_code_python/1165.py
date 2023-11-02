def solution():
    """Jerry needs to shingle 3 roofs. Each roof is made of two slanted rectangular sides measuring 20 feet by 40 feet. If he needs 8 shingles to cover one square foot of roof, how many shingles does he need total?"""
    # Define the dimensions of each roof in feet
    roof_width = 20
    roof_length = 40

    # Calculate the area of each roof in square feet
    roof_area = roof_width * roof_length * 2

    # Calculate the number of shingles needed for each roof
    shingles_per_sq_ft = 8
    shingles_per_roof = roof_area * shingles_per_sq_ft

    # Calculate the total number of shingles needed for all three roofs
    total_shingles = shingles_per_roof * 3

    # Display the total number of shingles
    result = total_shingles
    return result

print(solution())