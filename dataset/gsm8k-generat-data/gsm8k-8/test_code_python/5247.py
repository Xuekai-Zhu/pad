def solution():
    # Calculate the cost of the newspaper for Juanita on weekdays
    weekday_cost = 0.50 * 6
    # Calculate the cost of the newspaper for Juanita on Sunday
    sunday_cost = 2.00
    # Calculate the total cost of the newspaper for Juanita for a week
    weekly_cost = weekday_cost + sunday_cost
    # Calculate the cost of the newspaper for Juanita for a year
    yearly_cost = weekly_cost * 52
    # Calculate the difference between the cost for Juanita and the cost for Grant
    difference = yearly_cost - 200
    result = difference
    return result

print(solution())