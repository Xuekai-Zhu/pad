def solution():
    tv_price_increase = 2/5 # TV increases by 2/5 of its initial price
    phone_price_increase = 40/100 # Phone increases by 40% of its original price
    tv_price = 500 * (1 + tv_price_increase) # Calculate TV price after increase
    phone_price = 400 * (1 + phone_price_increase) # Calculate phone price after increase
    total_price = tv_price + phone_price # Calculate total price of both items after auction
    result = total_price
    return result

print(solution())