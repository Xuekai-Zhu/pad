def solution():
    # Define regular pay rate and overtime pay rate
    regular_rate = 5
    overtime_rate = 6

    # Calculate regular hours and overtime hours for each week
    week1_regular_hours = 40
    week1_overtime_hours = 4
    week2_regular_hours = 40
    week2_overtime_hours = 8

    # Calculate total pay for each week
    week1_pay = week1_regular_hours * regular_rate + week1_overtime_hours * overtime_rate
    week2_pay = week2_regular_hours * regular_rate + week2_overtime_hours * overtime_rate

    # Calculate total pay for two weeks
    total_pay = week1_pay + week2_pay

    # Round total_pay to two decimal places
    result = round(total_pay, 2)
    return result

print(solution())