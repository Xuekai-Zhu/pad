def solution():
    
    num_lollipops = 4
    num_chocolate = 6
    lollipop_price = 2
    chocolate_price = lollipop_price * 4

    total_cost = (num_lollipops * lollipop_price) + (num_chocolate * chocolate_price)
    total_payment = 6 * 10
    change = total_payment - total_cost
    result = change

    return result

print(solution())