def solution():
    # Calculate the total amount spent on croissants in a year
    saturday_cost = 3.50 * 52  # cost of regular croissant on Saturdays for a year
    sunday_cost = 5.50 * 52  # cost of almond croissant on Sundays for a year
    total_cost = saturday_cost + sunday_cost
    result = total_cost
    return result

print(solution())