def solution():
    """A new condo development has 23 floors. Regular floors have 12 units, whereas penthouse floors have only 2 units. If the top 2 floors are assigned for penthouse units, how many units does this condo have in total?"""
    regular_units_per_floor = 12
    penthouse_units_per_floor = 2
    regular_floors = 21
    penthouse_floors = 2
    total_regular_units = regular_floors * regular_units_per_floor
    total_penthouse_units = penthouse_floors * penthouse_units_per_floor
    total_units = total_regular_units + total_penthouse_units
    result = total_units
    return result

print(solution())