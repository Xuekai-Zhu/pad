def solution():
    # Calculate the total amount spent and refund received
    total_spent = 9 + 11 + 30  # Will bought a sweater for $9, a T-shirt for $11 and a pair of shoes for $30
    refund = 0.9 * 30  # Will returned his shoes for a 90% refund
    total_refund = refund
    amount_left = 74 - (total_spent - total_refund)  # Calculate the money Will has left

    result = amount_left
    return result

print(solution())