def solution():
    """John goes to the store and pays with a 20 dollar bill. He buys 3 sodas and gets $14 in change. How much did each soda cost?"""
    # Define the amount paid by John and the amount of change he received
    amount_paid = 20
    change_received = 14

    # Calculate the total cost of the sodas
    total_cost = amount_paid - change_received

    # Calculate the cost of each soda
    soda_cost = total_cost / 3

    # Return the result
    result = soda_cost
    return result

print(solution())