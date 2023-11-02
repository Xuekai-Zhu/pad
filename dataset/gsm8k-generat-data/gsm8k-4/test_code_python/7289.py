def solution():
    """Ursula bought five hot dogs at $1.50 each and three salads at $2.50 each. If she had two $10 bills, how much change did she get back?"""
    # Define the prices and quantities of hot dogs and salads
    hotdog_price = 1.5
    salad_price = 2.5
    hotdog_quantity = 5
    salad_quantity = 3

    # Calculate the total cost of the hot dogs and salads
    total_cost = (hotdog_price * hotdog_quantity) + (salad_price * salad_quantity)

    # Calculate the amount paid by Ursula
    amount_paid = 10 * 2

    # Calculate the change given back to Ursula
    change = amount_paid - total_cost

    result = change
    return result

print(solution())