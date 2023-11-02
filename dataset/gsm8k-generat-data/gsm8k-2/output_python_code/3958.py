def solution():
    """At the supermarket, the price paid for oranges is proportional to the mass purchased. Annie paid $6 for 2 kg of oranges. How much will Annie pay for 12 kg of oranges?"""
    price_per_kg = 6/2  # price per kg is $3
    total_price = price_per_kg * 12  # price for 12 kg of oranges
    result = total_price
    return result

print(solution())