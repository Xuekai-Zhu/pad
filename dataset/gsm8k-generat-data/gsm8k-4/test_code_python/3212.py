def solution():
    """A new condo development has 23 floors. Regular floors have 12 units, whereas penthouse floors have only 2 units. If the top 2 floors are assigned for penthouse units, how many units does this condo have in total?"""
    # Define the number of regular floors and penthouse floors
    regular_floors = 21
    penthouse_floors = 2

    # Calculate the number of regular units and penthouse units per floor
    regular_units_per_floor = 12
    penthouse_units_per_floor = 2

    # Calculate the number of regular units and penthouse units
    regular_units = regular_floors * regular_units_per_floor
    penthouse_units = penthouse_floors * penthouse_units_per_floor

    # Calculate the total number of units
    total_units = regular_units + penthouse_units

    result = total_units
    return result

print(solution())