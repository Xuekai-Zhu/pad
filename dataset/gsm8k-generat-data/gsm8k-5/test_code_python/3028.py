def solution():
    castles_on_marks_beach = 20
    towers_per_castle_on_marks_beach = 10
    castles_on_jeffs_beach = 3 * castles_on_marks_beach
    towers_per_castle_on_jeffs_beach = 5

    # Calculate total number of towers on Mark's beach
    towers_on_marks_beach = castles_on_marks_beach * towers_per_castle_on_marks_beach

    # Calculate total number of towers on Jeff's beach
    towers_on_jeffs_beach = castles_on_jeffs_beach * towers_per_castle_on_jeffs_beach

    # Calculate combined total number of sandcastles and towers
    combined_total = castles_on_marks_beach + castles_on_jeffs_beach + towers_on_marks_beach + towers_on_jeffs_beach
    result = combined_total
    return result

print(solution())