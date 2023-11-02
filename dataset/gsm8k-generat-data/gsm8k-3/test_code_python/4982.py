def solution():
    """Lee had $10 and his friend had $8. They went to a restaurant where they ordered chicken wings for $6 and a chicken salad for $4. They also got 2 sodas for $1.00 each. The tax came to $3. How much change should they have received in total?"""
    # Define the initial amount of money Lee and his friend have
    lee_money = 10
    friend_money = 8

    # Define the cost of each item
    chicken_wings_cost = 6
    chicken_salad_cost = 4
    soda_cost = 1
    tax = 3

    # Calculate the total cost of the meal
    total_cost = chicken_wings_cost + chicken_salad_cost + 2*soda_cost + tax

    # Calculate the change
    change = lee_money + friend_money - total_cost

    # Display the change
    result = change
    return result

print(solution())