def solution():
    cost_per_weekday = 0.50
    cost_per_weekend = 2.00
    number_of_weekdays = 3 
    number_of_weeks = 8
    total_cost = (cost_per_weekday * number_of_weekdays * number_of_weeks) + (cost_per_weekend * number_of_weeks)
    result = total_cost
    return result

print(solution())