def solution():
    sweaters_monday = 8
    sweaters_tuesday = sweaters_monday + 2
    sweaters_wednesday = sweaters_tuesday - 4
    sweaters_thursday = sweaters_tuesday - 4
    sweaters_friday = sweaters_monday / 2

    total_sweaters = sweaters_monday + sweaters_tuesday + sweaters_wednesday + sweaters_thursday + sweaters_friday
    result = total_sweaters
    return result

print(solution())