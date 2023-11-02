def solution():
    """Leila went to the supermarket to get some groceries. Then she headed to her mechanic to get her automobile fixed. If fixing her automobile cost $350 which was $50 more than thrice the amount she spent at the supermarket, how much has she spent altogether?"""
    # Let x be the amount Leila spent at the supermarket
    # Then, according to the problem, 3x + 50 = 350
    x = (350 - 50) / 3

    # Calculate the total amount Leila spent
    total_spent = x + 350

    # Display the total amount Leila spent
    result = total_spent
    return result

print(solution())