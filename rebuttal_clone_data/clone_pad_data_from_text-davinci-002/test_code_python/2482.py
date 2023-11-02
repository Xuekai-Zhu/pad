def solution():
    hem_length = 3
    stitches_per_minute = 24
    inches_per_foot = 12
    length_to_stitch = hem_length * inches_per_foot
    minutes_to_stitch = length_to_stitch / stitches_per_minute
    result = minutes_to_stitch
    return result

print(solution())