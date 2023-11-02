def solution():
    """Lee had $10 and his friend had $8. They went to a restaurant where they ordered chicken wings for $6
    and a chicken salad for $4. They also got 2 sodas for $1.00 each. The tax came to $3. How much change should 
    they have received in total?"""
    lee_money = 10
    friend_money = 8
    cost_of_food = 6 + 4 + 1 + 1
    tax = 3
    total_cost = cost_of_food + tax
    money_paid = lee_money + friend_money
    change = money_paid - total_cost
    result = change
    return result

print(solution())