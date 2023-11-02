def solution():
    
    snickers_cost = 1.5
    mms_cost = 3 * 2 * snickers_cost
    total_cost = 2 * snickers_cost + mms_cost
    money_given = 2 * 10
    change = money_given - total_cost
    result = change
    return result

print(solution())