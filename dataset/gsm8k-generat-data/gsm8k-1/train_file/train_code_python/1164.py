def solution():
    """Jerry needs to shingle 3 roofs. Each roof is made of two slanted rectangular sides measuring 20 feet by 40 feet. If he needs 8 shingles to cover one square foot of roof, how many shingles does he need total?"""
    num_roofs = 3
    width = 20
    length = 40
    area = 2 * width * length
    shingles_per_sqft = 8
    total_shingles = num_roofs * area * shingles_per_sqft
    result = total_shingles
    return result

print(solution())