def solution():
    """The house is 20.5 feet by 10 feet. The porch measures 6 feet by 4.5 feet. The house and the porch need shingles. How many square feet of shingles will be needed to roof the house and the porch?"""
    house_area = 20.5 * 10
    porch_area = 6 * 4.5
    total_area = house_area + porch_area
    # assuming 1 pack of shingles covers 32 square feet
    shingle_coverage = 32
    shingles_needed = total_area / shingle_coverage
    result = shingles_needed
    return result

print(solution())