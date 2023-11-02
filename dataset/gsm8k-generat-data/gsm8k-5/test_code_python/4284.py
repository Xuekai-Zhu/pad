def solution():
    jeff_pencils = 300
    jeff_donated = 0.3 * jeff_pencils  # Jeff donated 30% of his pencils
    jeff_remaining = jeff_pencils - jeff_donated  # Jeff has this many pencils remaining

    vicki_pencils = 2 * jeff_pencils  # Vicki has twice as many pencils as Jeff
    vicki_donated = 0.75 * vicki_pencils  # Vicki donated 75% of his pencils
    vicki_remaining = vicki_pencils - vicki_donated  # Vicki has this many pencils remaining

    total_remaining = jeff_remaining + vicki_remaining  # Total remaining pencils
    result = total_remaining
    return result

print(solution())