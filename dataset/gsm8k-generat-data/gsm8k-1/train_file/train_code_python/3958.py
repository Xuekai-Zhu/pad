def solution():
    """At the supermarket, the price paid for oranges is proportional to the mass purchased. Annie paid $6 for 2 kg of oranges. How much will Annie pay for 12 kg of oranges?"""
    price_per_kg = 6/2
    mass_purchased = 12
    total_cost = price_per_kg * mass_purchased
    result = total_cost
    return result

print(solution())