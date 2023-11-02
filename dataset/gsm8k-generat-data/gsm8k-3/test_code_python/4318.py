def solution():
    """Mell went to a cafeteria to spend some time with her friends. She ordered two cups of coffee and one piece of cake. Two of her friends ordered the same, but each of them also bought a bowl of ice cream. One cup of coffee is $4, one piece of cake is $7, and a bowl of ice cream is $3. How much money did Mell and her friends need to pay at the cafeteria?"""
    # Define the price of each item
    COFFEE_PRICE = 4
    CAKE_PRICE = 7
    ICECREAM_PRICE = 3

    # Calculate Mell's total cost
    mell_cost = 2*COFFEE_PRICE + CAKE_PRICE

    # Calculate the total cost for her two friends
    friends_cost = 2*(2*COFFEE_PRICE + CAKE_PRICE + ICECREAM_PRICE)

    # Calculate the total cost for everyone
    total_cost = mell_cost + friends_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())