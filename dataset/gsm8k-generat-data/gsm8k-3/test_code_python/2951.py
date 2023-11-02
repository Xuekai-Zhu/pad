def solution():
    """Anna sold 36 glasses of plain lemonade for $0.75 each.
    If she made $16 total from selling strawberry lemonade, how much more did she make from plain lemonade than strawberry?"""
    # Define the number of glasses of plain lemonade sold and the price per glass
    plain_lemonade_glasses = 36
    plain_lemonade_price = 0.75

    # Calculate the total revenue from plain lemonade
    plain_lemonade_revenue = plain_lemonade_glasses * plain_lemonade_price

    # Calculate the revenue from strawberry lemonade
    strawberry_lemonade_revenue = 16

    # Calculate the difference in revenue between plain and strawberry lemonade
    revenue_difference = plain_lemonade_revenue - strawberry_lemonade_revenue

    # Display the difference in revenue
    result = revenue_difference
    return result

print(solution())