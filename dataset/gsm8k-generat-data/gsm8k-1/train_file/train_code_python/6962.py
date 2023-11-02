def solution():
    """Leila went to the supermarket to buy food for the Christmas party. She bought apples for 5€, sugar for 3€ and carrots for 17€. She paid with a 50€ bill. How much money does the saleswoman return to her?"""
    total_cost = 5 + 3 + 17
    amount_paid = 50
    change = amount_paid - total_cost
    result = change
    return result

print(solution())