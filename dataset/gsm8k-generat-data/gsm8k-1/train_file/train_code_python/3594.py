def solution():
    """Calculate the total amount of money Mr. Sergio got in a particular season selling fruits at $50 per kg, given that his farm produced 400 kg of mangoes, and the total produce of apples was twice the total produce of mangoes, and the total produce of oranges was 200 kg more than that of mangoes."""
    mangoes = 400
    apples = mangoes * 2
    oranges = mangoes + 200
    total_produce = mangoes + apples + oranges
    price_per_kg = 50
    total_money = total_produce * price_per_kg
    
    return total_money

print(solution())