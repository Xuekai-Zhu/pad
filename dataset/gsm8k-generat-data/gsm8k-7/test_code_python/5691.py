def solution():
    appetizer_cost = 8
    steak_price = 20
    wine_price = 3
    dessert_price = 6

    # Apply the 50% voucher discount to the steak
    steak_price *= 0.5

    # Calculate the total cost of the meal, without the tip
    total_cost = appetizer_cost + steak_price + (2 * wine_price) + dessert_price

    # Calculate the tip, based on the full cost of the meal without the discount
    tip = 0.2 * (appetizer_cost + 20 + (2 * wine_price) + dessert_price)

    # Calculate the total cost including the tip
    total_cost += tip
    result = total_cost
    return result

print(solution())