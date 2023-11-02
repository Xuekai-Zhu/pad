def solution():
    """Anna sold 36 glasses of plain lemonade for $0.75 each. If she made $16 total from selling strawberry lemonade, how much more did she make from plain lemonade than strawberry?"""
    plain_lemonade_glasses = 36
    plain_lemonade_price = 0.75
    plain_lemonade_earnings = plain_lemonade_glasses * plain_lemonade_price
    total_earnings = plain_lemonade_earnings + 16
    strawberry_lemonade_earnings = total_earnings / 2
    difference = plain_lemonade_earnings - strawberry_lemonade_earnings
    result = difference
    return result

print(solution())