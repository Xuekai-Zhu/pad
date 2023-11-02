def solution():
    """Joan is at the grocery store. She has a total of $60 to spend. She is going to purchase 2 containers of hummus, which are $5 each. She is going to purchase chicken for $20, bacon for $10, and vegetables for $10. She wants to purchase apples which are $2 each. With her remaining money, how many apples can she purchase?"""
    total_budget = 60
    cost_of_hummus = 5 * 2
    cost_of_chicken = 20
    cost_of_bacon = 10
    cost_of_vegetables = 10
    total_spent = cost_of_hummus + cost_of_chicken + cost_of_bacon + cost_of_vegetables
    remaining_budget = total_budget - total_spent
    apples_cost = 2
    no_of_apples = remaining_budget // apples_cost
    result = no_of_apples

    return result

print(solution())