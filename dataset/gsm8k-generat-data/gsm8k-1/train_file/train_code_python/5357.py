def solution():
    """A store offers a $2 discount for every $10 purchase on any item in the store. Kataleya went to the store and bought 400 peaches sold at forty cents each. Calculate the total amount of money she paid at the store for the fruits."""
    peach_price = 0.4
    num_peaches = 400
    peach_cost = peach_price * num_peaches
    discount = (peach_cost // 10) * 2
    total_cost = peach_cost - discount
    result = total_cost
    return result

print(solution())