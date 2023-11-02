def solution():
    """Bob gets paid $5 an hour for the regular hours he works and $6 an hour for any overtime hours he works. All hours over 40 in a week are considered overtime. If Bob works 44 hours in the first week and 48 hours in the second week, how much did he make?"""
    # Define regular and overtime pay rates
    REGULAR_RATE = 5
    OVERTIME_RATE = 6

    # Define number of regular and overtime hours worked in week 1
    week_1_regular_hours = 40
    week_1_overtime_hours = 4

    # Calculate earnings for week 1
    week_1_earnings = (week_1_regular_hours * REGULAR_RATE) + (week_1_overtime_hours * OVERTIME_RATE)

    # Define number of regular and overtime hours worked in week 2
    week_2_regular_hours = 40
    week_2_overtime_hours = 8

    # Calculate earnings for week 2
    week_2_earnings = (week_2_regular_hours * REGULAR_RATE) + (week_2_overtime_hours * OVERTIME_RATE)

    # Calculate total earnings for both weeks
    total_earnings = week_1_earnings + week_2_earnings

    # Display total earnings
    result = total_earnings
    return result

print(solution())