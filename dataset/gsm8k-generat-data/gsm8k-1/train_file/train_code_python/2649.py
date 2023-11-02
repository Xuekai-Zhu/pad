def solution():
    """Jack has $45 and 36 euros. If each euro is worth two dollars, how much money does he have total in dollars?"""
    dollars_amount = 45
    euro_amount = 36
    exchange_rate = 2
    total_dollars = dollars_amount + (euro_amount * exchange_rate)
    result = total_dollars
    return result

print(solution())