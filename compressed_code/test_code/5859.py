def solution():
    
    beef_pounds = 1000
    beef_price_per_pound = 8
    chicken_pounds = beef_pounds * 2
    chicken_price_per_pound = 3
    total_cost = (beef_pounds * beef_price_per_pound) + (chicken_pounds * chicken_price_per_pound)
    result = total_cost
    return result

print(solution())