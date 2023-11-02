def solution():
    """Mr. Sergio is a fruit grower producing apples, mangoes and oranges. In a particular season, the total produce of apples was twice the total produce of mangoes, and the total produce of oranges was 200 kg more than that of mangoes. If his farm produced 400 kg of mangoes and he sold the fruits at $50 per kg,  calculate the total amount of money he got in that season."""
    # Define the price per kg of mangoes
    price_per_kg = 50

    # Calculate the total produce of apples
    apples_produce = 2 * 400

    # Calculate the total produce of oranges
    oranges_produce = 400 + 200

    # Calculate the total produce of all fruits
    total_produce = apples_produce + 400 + oranges_produce

    # Calculate the total amount of money Mr. Sergio got from selling the fruits
    total_money = total_produce * price_per_kg

    # Return the result
    result = total_money
    return result

print(solution())