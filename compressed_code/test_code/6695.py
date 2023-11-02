def solution():
    
    num_roofs = 3
    width = 20
    length = 40
    area = 2 * width * length
    shingles_per_sqft = 8
    total_shingles = num_roofs * area * shingles_per_sqft
    result = total_shingles
    return result

print(solution())