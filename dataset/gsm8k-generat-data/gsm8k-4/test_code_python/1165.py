def solution():
    """Jerry needs to shingle 3 roofs. Each roof is made of two slanted rectangular sides measuring 20 feet by 40 feet. If he needs 8 shingles to cover one square foot of roof, how many shingles does he need total?"""
    # Define the dimensions of each roof
    length = 20
    width = 40
    area = length * width * 2

    # Calculate the total area of all three roofs
    total_area = area * 3

    # Calculate the total number of shingles needed
    shingles_per_sqft = 8
    total_shingles = total_area * shingles_per_sqft

    # return the result
    result = total_shingles
    return result

print(solution())