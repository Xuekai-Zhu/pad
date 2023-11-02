def solution():
    
    beef_pounds = 1000
    beef_price_per_pound = 8
    chicken_pounds = 2 * beef_pounds
    chicken_price_per_pound = 3
    beef_cost = beef_pounds * beef_price_per_pound
    chicken_cost = chicken_pounds * chicken_price_per_pound
    total_cost = beef_cost + chicken_cost
    result = total_cost
    return result

print(solution())