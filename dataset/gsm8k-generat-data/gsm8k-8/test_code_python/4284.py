def solution():
    # Jeff's initial number of pencils
    jeff_pencils = 300

    # Jeff's donated pencils
    jeff_donated = 0.3 * jeff_pencils

    # Jeff's remaining pencils
    jeff_remaining = jeff_pencils - jeff_donated

    # Vicki's initial number of pencils
    vicki_pencils = 2 * jeff_pencils

    # Vicki's donated pencils
    vicki_donated = 0.75 * vicki_pencils

    # Vicki's remaining pencils
    vicki_remaining = vicki_pencils - vicki_donated

    # Total remaining pencils
    total_remaining = jeff_remaining + vicki_remaining
    result = total_remaining
    return result

print(solution())