def solution():
    # Define the price and quantity of each CD type
    rock_price = 5
    pop_price = 10
    dance_price = 3
    country_price = 7

    rock_qty = 4
    pop_qty = 4
    dance_qty = 4
    country_qty = 4

    # Calculate the total cost of the CDs
    total_cost = (rock_price * rock_qty) + (pop_price * pop_qty) + (dance_price * dance_qty) + (country_price * country_qty)

    # Calculate how much money Julia is short
    short_amount = total_cost - 75
    result = short_amount
    return result

print(solution())