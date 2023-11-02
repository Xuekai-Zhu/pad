def solution():
    
    school_price = 45
    discount_percent = 20
    outside_price = school_price - (school_price * (discount_percent / 100))
    total_cost = 3 * outside_price
    savings = (3 * school_price) - total_cost
    result = savings
    return result

print(solution())