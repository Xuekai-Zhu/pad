def solution():
    """John books 3 nights at a hotel room for $250 a night. He has a $100 discount. How much does he pay?"""
    nights = 3
    price_per_night = 250
    discount = 100
    total_price = (nights * price_per_night) - discount
    result = total_price
    return result

print(solution())