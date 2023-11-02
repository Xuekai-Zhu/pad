def solution():
    """A store offers a $2 discount for every $10 purchase on any item in the store. Kataleya went to the store and bought 400 peaches sold at forty cents each. Calculate the total amount of money she paid at the store for the fruits."""
    peaches_price = 0.4
    peaches_quantity = 400
    total_peaches_price = peaches_price * peaches_quantity
    discount_amount = (int(total_peaches_price / 10)) * 2
    final_price = total_peaches_price - discount_amount
    result = final_price
    return result

print(solution())