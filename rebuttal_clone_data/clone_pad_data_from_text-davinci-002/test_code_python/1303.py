def solution():
    monday_cost = 6
    tuesday_cost = monday_cost * 2
    wednesday_cost = monday_cost + tuesday_cost
    total_cost = monday_cost + tuesday_cost + wednesday_cost
    result = total_cost
    return result

print(solution())