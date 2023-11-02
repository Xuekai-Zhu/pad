def solution():
    # Define the amount of silver and gold purchased
    silver_amount = 1.5 #ounces
    gold_amount = 2 * silver_amount #ounces

    # Calculate the cost of the silver and gold
    silver_cost = silver_amount * 20 #$ per ounce
    gold_cost = gold_amount * 20 * 50 #$ per ounce (50 times more expensive)

    # Calculate the total cost
    total_cost = silver_cost + gold_cost
    result = total_cost
    return result

print(solution())