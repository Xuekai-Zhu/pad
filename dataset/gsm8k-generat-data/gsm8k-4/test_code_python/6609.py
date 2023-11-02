def solution():
    """John buys 5 toys that each cost $3. He gets a 20% discount. How much did he pay for everything?"""
    # Define the cost of one toy and the number of toys
    TOY_COST = 3
    NUM_TOYS = 5

    # Calculate the total cost before discount
    total_cost_before_discount = TOY_COST * NUM_TOYS

    # Calculate the discounted cost
    discount_amount = total_cost_before_discount * 0.2
    total_cost_after_discount = total_cost_before_discount - discount_amount

    # return the result
    result = total_cost_after_discount
    return result

print(solution())