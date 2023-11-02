def solution():
    josh_hours_per_day = 8
    carl_hours_per_day = josh_hours_per_day - 2
    josh_rate = 9
    carl_rate = josh_rate / 2
    num_weeks = 4
    num_days_per_week = 5

    # Calculate the total number of hours worked by Josh in one month
    josh_total_hours = josh_hours_per_day * num_days_per_week * num_weeks

    # Calculate the total number of hours worked by Carl in one month
    carl_total_hours = carl_hours_per_day * num_days_per_week * num_weeks

    # Calculate the total cost of Josh's salary in one month
    josh_salary = josh_total_hours * josh_rate

    # Calculate the total cost of Carl's salary in one month
    carl_salary = carl_total_hours * carl_rate

    # Calculate the total cost for both Josh and Carl in one month
    total_salary = josh_salary + carl_salary
    result = total_salary
    return result

print(solution())