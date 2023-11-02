def solution():
    """Ursula bought five hot dogs at $1.50 each and three salads at $2.50 each. If she had two $10 bills, how much change did she get back?"""
    # Define the prices of the hot dogs and salads
    HOTDOG_PRICE = 1.5
    SALAD_PRICE = 2.5

    # Define the number of hot dogs and salads purchased
    hotdogs = 5
    salads = 3

    # Calculate the total cost of the hot dogs and salads
    total_cost = hotdogs * HOTDOG_PRICE + salads * SALAD_PRICE

    # Calculate the amount paid by Ursula
    amount_paid = 10 * 2

    # Calculate the change Ursula received
    change = amount_paid - total_cost

    # Display the change Ursula received
    result = change
    return result

print(solution())