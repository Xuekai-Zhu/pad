def solution():
    """Stella’s antique shop has 3 dolls, 2 clocks and 5 glasses for sale. She sells the dolls for $5 each. The clocks are priced at $15 each. The glasses are priced at $4 each. If she spent $40 to buy everything and she sells all of her merchandise, how much profit will she make?"""
    # Define the number of each item for sale
    num_dolls = 3
    num_clocks = 2
    num_glasses = 5

    # Define the selling price of each item
    doll_price = 5
    clock_price = 15
    glass_price = 4

    # Calculate the total revenue from selling all items
    total_revenue = (num_dolls * doll_price) + (num_clocks * clock_price) + (num_glasses * glass_price)

    # Calculate the cost to buy all items
    total_cost = 40

    # Calculate the profit from selling all items
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())