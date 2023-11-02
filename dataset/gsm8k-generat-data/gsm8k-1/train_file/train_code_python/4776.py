def solution():
    """ Big Lots is having a sale. All chairs are 25% off. If you buy more than 5 chairs, you get an additional 1/3 off the discounted price of the number of chairs over 5. If you bought 8 chairs that were normally priced at $20, how much do the chairs cost in total?"""
    original_price = 20
    discounted_price = original_price * 0.75 # 25% off

    if discounted_price < original_price:
        discounted_price = original_price

    num_chairs = 8
    num_discounted_chairs = max(num_chairs - 5, 0)
    
    discounted_chair_price = discounted_price * (2/3) # additional 1/3 off

    total_price = (discounted_price * (num_chairs - num_discounted_chairs)) + (discounted_chair_price * num_discounted_chairs)
    
    return total_price

print(solution())