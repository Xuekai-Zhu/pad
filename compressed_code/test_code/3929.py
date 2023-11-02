def solution():
    
    tv_price = 500
    phone_price = 400
    tv_increase = 2/5 * tv_price
    tv_total_price = tv_price + tv_increase
    phone_increase = 0.4 * phone_price
    phone_total_price = phone_price + phone_increase
    total_price = tv_total_price + phone_total_price
    result = total_price
    return result

print(solution())