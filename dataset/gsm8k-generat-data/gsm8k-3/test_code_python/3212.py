def solution():
    """A new condo development has 23 floors. Regular floors have 12 units, whereas penthouse floors have only 2 units. If the top 2 floors are assigned for penthouse units, how many units does this condo have in total?"""
    # Define the number of regular floors and penthouse floors
    REGULAR_FLOORS = 21
    PENTHOUSE_FLOORS = 2

    # Define the number of units per regular and penthouse floor
    REGULAR_UNITS = 12
    PENTHOUSE_UNITS = 2

    # Calculate the total number of regular units
    regular_units = REGULAR_FLOORS * REGULAR_UNITS

    # Calculate the total number of penthouse units
    penthouse_units = PENTHOUSE_FLOORS * PENTHOUSE_UNITS

    # Calculate the total number of units
    total_units = regular_units + penthouse_units

    # Display the total number of units
    result = total_units
    return result

print(solution())