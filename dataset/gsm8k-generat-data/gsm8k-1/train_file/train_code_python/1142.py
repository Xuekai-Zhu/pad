def solution():
    """The price of buying a wooden toy at the new Craftee And Best store is $20, and the cost of buying a hat is $10. If Kendra went to the shop with a $100 bill and bought two wooden toys and three hats, calculate the change she received."""
    wooden_toy_price = 20
    hat_price = 10
    total_cost = (2 * wooden_toy_price) + (3 * hat_price)
    payment = 100
    change = payment - total_cost
    result = change
    return result

print(solution())