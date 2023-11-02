def solution():
    """Lee had $10 and his friend had $8. They went to a restaurant where they ordered chicken wings for $6 and a chicken salad for $4. They also got 2 sodas for $1.00 each. The tax came to $3. How much change should they have received in total?"""
    # Define the initial amount of money Lee and his friend have
    lee_money = 10
    friend_money = 8

    # Define the prices of the food and drinks
    wings_price = 6
    salad_price = 4
    soda_price = 1
    tax = 3

    # Calculate the total cost of the meal
    total_cost = wings_price + salad_price + 2 * soda_price + tax

    # Calculate the total money available
    total_money = lee_money + friend_money

    # Calculate the change
    change = total_money - total_cost

    result = change
    return result

print(solution())