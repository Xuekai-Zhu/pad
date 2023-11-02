def solution():
    """Enrique earns a 15% commission on every piece of clothing item he sells. In one day he sells 2 $700.00 suits, 6 shirts that cost $50.00 each and 2 pairs of loafers that are $150.00 each. How much commission does Enrique earn?"""
    suits_sold = 2
    suit_price = 700
    shirt_sold = 6
    shirt_price = 50
    loafers_sold = 2
    loafers_price = 150
    
    total_sales = (suits_sold * suit_price) + (shirt_sold * shirt_price) + (loafers_sold * loafers_price)
    commission_rate = 0.15
    commission_earned = total_sales * commission_rate
    result = commission_earned
    
    return result

print(solution())