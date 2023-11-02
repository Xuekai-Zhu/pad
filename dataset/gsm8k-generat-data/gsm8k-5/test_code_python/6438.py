def solution():
    total_legs = 40  # The woodworker has made 40 furniture legs
    legs_per_chair = 4  # Each chair has 4 legs
    chairs_built = 6  # The woodworker has built 6 chairs

    # Calculate the total number of legs used for the chairs
    legs_for_chairs = legs_per_chair * chairs_built

    # Calculate the total number of legs used for the tables
    legs_for_tables = total_legs - legs_for_chairs

    # Calculate the number of tables made
    legs_per_table = 4  # Each table has 4 legs
    tables_made = legs_for_tables // legs_per_table

    result = tables_made
    return result

print(solution())