def solution():
    """Genevieve picked some cherries from the supermarket shelves that cost $8 per kilogram. When Genevieve reached the checkout counter, she realized she was $400 short of the total price and her friend Clarice chipped in. If Genevieve had $1600 on her, how many kilograms of cherries did she buy?"""
    price_per_kg = 8
    total_price = 1600 + 400
    amount_paid = 1600
    amount_owed = total_price - amount_paid
    kg_bought = amount_owed / price_per_kg
    result = kg_bought
    return result

print(solution())