def solution():
    """Blake bought 4 lollipops and 6 packs of chocolate. If each lollipop costs $2 and a pack of chocolate costs the same as four lollipops, how much change will Blake get back if he gave the cashier 6 $10 bills?"""
    # Define the cost of each lollipop and pack of chocolate
    LOLLIPOP_PRICE = 2
    CHOCOLATE_PRICE = 8  # 4 lollipops cost the same as 1 pack of chocolate

    # Calculate the total cost of the lollipops
    lollipop_cost = 4 * LOLLIPOP_PRICE

    # Calculate the total cost of the chocolate packs
    chocolate_cost = 6 * CHOCOLATE_PRICE

    # Calculate the total cost of all the items
    total_cost = lollipop_cost + chocolate_cost

    # Calculate the amount of money Blake gave to the cashier
    amount_paid = 6 * 10

    # Calculate the change Blake will get back
    change = amount_paid - total_cost

    # Display the change
    result = change
    return result

print(solution())