def solution():
    """Stella’s antique shop has 3 dolls, 2 clocks and 5 glasses for sale. She sells the dolls for $5 each. The clocks are priced at $15 each. The glasses are priced at $4 each. If she spent $40 to buy everything and she sells all of her merchandise, how much profit will she make?"""
    # Define the cost and selling price of each item
    doll_cost = 0
    doll_price = 5
    clock_cost = 0
    clock_price = 15
    glass_cost = 0
    glass_price = 4

    # Calculate the total cost and selling price of the merchandise
    total_cost = (3 * doll_cost) + (2 * clock_cost) + (5 * glass_cost) + 40
    total_price = (3 * doll_price) + (2 * clock_price) + (5 * glass_price)

    # Calculate the profit
    profit = total_price - total_cost

    result = profit
    return result

print(solution())