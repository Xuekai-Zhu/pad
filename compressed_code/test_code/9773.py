def solution():
    
    tv_cost = 500
    tv_increase = tv_cost * (2/5)
    tv_price = tv_cost + tv_increase
    
    phone_cost = 400
    phone_increase = phone_cost * 0.4
    phone_price = phone_cost + phone_increase
    
    total_amount = tv_price + phone_price
    result = total_amount
    return result

print(solution())