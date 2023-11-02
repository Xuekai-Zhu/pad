def solution():
    phone_cost = 1000
    monthly_cost = 200
    case_cost = phone_cost * 0.2
    headphone_cost = case_cost / 2
    total_cost = phone_cost + monthly_cost + case_cost + headphone_cost
    result = total_cost
    return result

print(solution())