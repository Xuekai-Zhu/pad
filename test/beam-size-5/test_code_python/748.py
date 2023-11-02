def solution():
    
    num_roommates = 4
    monthly_bill = 100
    months_per_year = 12
    total_cost = num_roommates * monthly_bill * months_per_year
    cost_per_roommate = total_cost / num_roommates
    result = cost_per_roommate
    return result

print(solution())