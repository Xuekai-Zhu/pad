def solution():
    """Leila went to the supermarket to get some groceries. Then she headed to her mechanic to get her automobile fixed.
    If fixing her automobile cost $350 which was $50 more than thrice the amount she spent at the supermarket, how much has she spent altogether?"""
    x = (350 - 50) / 3  # calculate the amount spent at the supermarket
    total_spent = x + 350  # calculate the total amount spent
    result = total_spent
    return result

print(solution())