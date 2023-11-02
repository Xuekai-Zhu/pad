def solution():
    """Mr. Sergio is a fruit grower producing apples, mangoes and oranges. In a particular season, the total produce of apples was twice the total produce of mangoes, and the total produce of oranges was 200 kg more than that of mangoes. If his farm produced 400 kg of mangoes and he sold the fruits at $50 per kg,  calculate the total amount of money he got in that season."""
    # Calculate the total produce of apples
    apple_produce = 2 * 400

    # Calculate the total produce of oranges
    orange_produce = 400 + 200

    # Calculate the total produce of all fruits
    total_produce = apple_produce + 400 + orange_produce

    # Calculate the total amount of money received
    total_money = total_produce * 50

    # Display the total amount of money received
    result = total_money
    return result

print(solution())