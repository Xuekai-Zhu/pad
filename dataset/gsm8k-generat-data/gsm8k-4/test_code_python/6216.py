def solution():
    """The school decided to add 20% to the gym budget. In a normal month, they could buy 15 dodgeballs for $5 each if they spent the entire budget on that. If they only buy softballs instead, which cost $9 each, how many can they buy with the new budget?"""
    # Define the original budget and the increase percentage
    original_budget = 0
    increase_percentage = 20

    # Calculate the new budget
    new_budget = original_budget * (1 + increase_percentage / 100)

    # Calculate the number of softballs that can be purchased with the new budget
    softball_price = 9
    softball_quantity = new_budget // softball_price

    # return the result
    result = softball_quantity
    return result

print(solution())