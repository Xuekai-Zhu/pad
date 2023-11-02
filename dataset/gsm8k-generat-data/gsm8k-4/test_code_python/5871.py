def solution():
    """Tayzia and her two young daughters get haircuts. Women’s haircuts are $48. Children’s haircuts are $36. If Tayzia wants to give a 20% tip to the hair stylist, how much would it be?"""
    # Define the prices for women's and children's haircuts
    women_price = 48
    children_price = 36

    # Calculate the total cost of haircuts for Tayzia and her daughters
    total_cost = 2 * women_price + 2 * children_price 

    # Calculate the tip amount
    tip = 0.2 * total_cost

    # Calculate the total cost with the tip included
    total_cost_with_tip = total_cost + tip

    # return the result
    result = tip
    return result

print(solution())