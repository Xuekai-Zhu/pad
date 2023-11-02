def solution():
    """Mrs. Tatiana owns a grocery store that sells different fruits and vegetables, which includes carrots. The price of carrots in the grocery store increases by 5% of the original price every year. What would be the price of carrots after three years if it was $120 initially? (Round to the nearest integer)"""
    initial_price = 120
    price_increase = 0.05
    years = 3
    new_price = initial_price * (1 + price_increase)**years
    result = round(new_price)
    return result

print(solution())