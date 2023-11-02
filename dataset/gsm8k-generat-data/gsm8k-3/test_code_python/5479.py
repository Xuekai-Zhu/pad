def solution():
    """A guy goes to the tool shop and buys 5 sets of drill bits. Each set costs 6 dollars. He then pays 10% tax on the order. What was the total amount he paid?"""
    # Define the cost of each set of drill bits
    DRILL_SET_PRICE = 6
    
    # Define the number of sets purchased
    sets_purchased = 5
    
    # Calculate the cost before tax
    cost_before_tax = DRILL_SET_PRICE * sets_purchased
    
    # Calculate the amount of tax
    tax = cost_before_tax * 0.1
    
    # Calculate the total cost after tax
    total_cost = cost_before_tax + tax
    
    # Display the total cost
    result = total_cost
    return result

print(solution())