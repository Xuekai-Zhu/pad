def solution():
    
    hem_length = 3 * 12 
    stitch_length = 1/4
    stitches_needed = hem_length / stitch_length
    stitches_per_minute = 24
    time_needed = stitches_needed / stitches_per_minute
    result = time_needed
    return result

print(solution())