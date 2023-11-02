def solution():
    """Anna sold 36 glasses of plain lemonade for $0.75 each. If she made $16 total from selling strawberry lemonade, how much more did she make from plain lemonade than strawberry?"""
    # Define the number of glasses of plain lemonade sold and the price per glass
    plain_lemonade_glasses = 36
    plain_lemonade_price = 0.75

    # Calculate the total earnings from selling plain lemonade
    plain_lemonade_earnings = plain_lemonade_glasses * plain_lemonade_price

    # Calculate the earnings from selling strawberry lemonade
    strawberry_lemonade_earnings = 16

    # Calculate the difference in earnings between plain and strawberry lemonade
    difference = plain_lemonade_earnings - strawberry_lemonade_earnings

    result = difference
    return result

print(solution())