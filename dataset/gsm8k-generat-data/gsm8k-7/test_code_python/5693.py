def solution():
    sweaters_on_monday = 8
    sweaters_on_tuesday = sweaters_on_monday + 2
    sweaters_on_wednesday = sweaters_on_tuesday - 4
    sweaters_on_thursday = sweaters_on_tuesday - 4
    sweaters_on_friday = sweaters_on_monday / 2

    total_sweaters = sweaters_on_monday + sweaters_on_tuesday + sweaters_on_wednesday + sweaters_on_thursday + sweaters_on_friday
    result = total_sweaters
    return result

print(solution())