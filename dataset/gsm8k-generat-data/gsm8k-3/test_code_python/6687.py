def solution():
    """John goes to the store and pays with a 20 dollar bill. He buys 3 sodas and gets $14 in change. How much did each soda cost?"""
    # Define the total amount paid by John
    total_paid = 20

    # Define the total change received by John
    total_change = 14

    # Calculate the total cost of the sodas
    soda_cost_total = total_paid - total_change

    # Calculate the cost per soda
    soda_cost_each = soda_cost_total / 3

    # Display the cost per soda
    result = soda_cost_each
    return result

print(solution())