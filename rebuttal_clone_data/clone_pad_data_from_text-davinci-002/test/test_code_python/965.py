def solution():
    length = 600
    width = 400
    laps = 10
    skipped_laps = 2
    total_laps = laps - skipped_laps
    perimeter = (2 * length) + (2 * width)
    total_distance = total_laps * perimeter
    result = total_distance
    return result

print(solution())