def solution():
    """Mell went to a cafeteria to spend some time with her friends. She ordered two cups of coffee and one piece of cake. Two of her friends ordered the same, but each of them also bought a bowl of ice cream. One cup of coffee is $4, one piece of cake is $7, and a bowl of ice cream is $3. How much money did Mell and her friends need to pay at the cafeteria?"""
    # Define the prices of coffee, cake, and ice cream
    COFFEE_PRICE = 4
    CAKE_PRICE = 7
    ICE_CREAM_PRICE = 3

    # Calculate the total cost of Mell's order
    mell_cost = (2 * COFFEE_PRICE) + CAKE_PRICE

    # Calculate the total cost of each friend's order
    friend_cost = mell_cost + (2 * ICE_CREAM_PRICE)

    # Calculate the total cost for Mell and her friends
    total_cost = mell_cost + (2 * friend_cost)

    result = total_cost
    return result

print(solution())