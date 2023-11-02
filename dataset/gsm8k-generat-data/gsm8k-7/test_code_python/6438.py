def solution():
    total_legs = 40
    num_chairs = 6
    legs_per_chair = 4
    legs_per_table = 4

    # Calculate the total number of legs used for the chairs
    total_legs_chairs = num_chairs * legs_per_chair

    # Calculate the remaining legs after making the chairs
    remaining_legs = total_legs - total_legs_chairs

    # Calculate the number of tables that can be made with the remaining legs
    num_tables = remaining_legs / legs_per_table
    result = num_tables
    return result

print(solution())