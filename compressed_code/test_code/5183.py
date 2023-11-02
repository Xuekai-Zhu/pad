def solution():
    
    dress_price = 20
    pants_price = 12
    jacket_price = 30
    transport_cost = 5
    total_cost = (5 * dress_price) + (3 * pants_price) + (4 * jacket_price) + transport_cost
    initial_fund = 400
    remaining_fund = initial_fund - total_cost
    result = remaining_fund
    return result

print(solution())