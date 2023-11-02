def solution():
    
    roof_width = 20
    roof_length = 40
    roof_area = 2 * roof_width * roof_length
    shingles_per_sq_ft = 8
    shingles_per_roof = roof_area * shingles_per_sq_ft
    total_shingles = shingles_per_roof * 3
    result = total_shingles
    return result

print(solution())