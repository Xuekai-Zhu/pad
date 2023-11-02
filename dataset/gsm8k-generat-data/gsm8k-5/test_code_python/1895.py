def solution():
    # Kilometers ridden on Monday and Tuesday
    km_monday = 40
    km_tuesday = 50

    # Kilometers ridden on Wednesday is 50% less than on Tuesday
    km_wednesday = 0.5 * km_tuesday

    # Kilometers ridden on Thursday is the sum of Monday and Wednesday
    km_thursday = km_monday + km_wednesday

    # Total kilometers ridden in the competition
    total_km = km_monday + km_tuesday + km_wednesday + km_thursday
    result = total_km
    return result

print(solution())