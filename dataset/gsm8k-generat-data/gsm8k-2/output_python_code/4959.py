def solution():
    """Leticia, Scarlett, and Percy decide to eat at a Greek restaurant for lunch. The prices for their dishes cost $10, $13, and $17, respectively. If the trio gives the waiter a 10% tip, how much gratuity should the waiter receive in dollars?"""
    leticia_price = 10
    scarlett_price = 13
    percy_price = 17
    total_price = leticia_price + scarlett_price + percy_price
    tip_percentage = 0.1
    tip_amount = total_price * tip_percentage
    result = tip_amount
    return result

print(solution())