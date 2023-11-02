def solution():
    number_of_students = 35
    number_of_chaperones = 5
    number_of_lunches = number_of_students + number_of_chaperones + 3
    cost_per_lunch = 7
    total_cost = number_of_lunches * cost_per_lunch
    result = total_cost
    return result

print(solution())