def solution():
    """Patrick has been saving money to buy a bicycle that costs $150. He saved half the price but he then lent $50 to his friend. How much money does Patrick have now?"""
    # Define the cost of the bicycle and the amount Patrick saved
    bicycle_cost = 150
    amount_saved = bicycle_cost / 2

    # Subtract the amount Patrick lent to his friend
    amount_saved -= 50

    # Return the remaining amount Patrick has saved
    result = amount_saved
    return result

print(solution())