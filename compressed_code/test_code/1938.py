def solution():
    
    hem_length = 3 * 12  
    stitch_length = 1 / 4
    stitches_per_inch = 1 / stitch_length
    total_stitches = hem_length * stitches_per_inch
    stitch_time = 1 / 24  
    total_time = total_stitches * stitch_time
    result = total_time
    return result

print(solution())