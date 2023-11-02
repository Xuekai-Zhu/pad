def solution():
    """James was doing some shopping in his favorite shop and he saw an offer on shoes that give him a second pair of shoes for half 
    off the original price. He took the offer and took the first pair of shoes for $40 and the second one for $60. At the cashier, 
    the lady told him that the offer applies strictly to the cheaper pair of shoes, and also that he was selected for an extra discount 
    of a fourth off the total amount. How much money did James end up paying for both pairs of shoes?"""
    # calculate original cost of both pairs of shoes
    first_pair_cost = 40
    second_pair_cost = 60
    original_cost = first_pair_cost + second_pair_cost
    
    # apply discount to cheaper pair of shoes
    if first_pair_cost <= second_pair_cost:
        discounted_pair_cost = first_pair_cost * 0.5
        undiscounted_pair_cost = second_pair_cost
    else:
        discounted_pair_cost = second_pair_cost * 0.5
        undiscounted_pair_cost = first_pair_cost
    
    # apply extra discount to total amount
    total_discounted_cost = undiscounted_pair_cost + discounted_pair_cost
    final_cost = total_discounted_cost - (total_discounted_cost * 0.25)
    
    result = final_cost
    return result

print(solution())