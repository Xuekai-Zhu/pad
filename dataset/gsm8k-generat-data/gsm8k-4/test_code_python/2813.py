def solution():
    """Leila went to the supermarket to get some groceries. Then she headed to her mechanic to get her automobile fixed. If fixing her automobile cost $350 which was $50 more than thrice the amount she spent at the supermarket, how much has she spent altogether?"""
    # Define the amount spent at the supermarket
    supermarket_spending = None

    # Calculate the amount spent at the supermarket using the given relationship
    supermarket_spending = (350 - 50) / 3

    # Calculate the total amount spent
    total_spending = supermarket_spending + 350

    result = total_spending
    return result

print(solution())