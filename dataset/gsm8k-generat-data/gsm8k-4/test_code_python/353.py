def solution():
    """On Friday, Remy paid Sally’s Woodworking LLC a total of $20,700 for 150 pieces of furniture. Later that evening, the company’s accountant discovered that a new intern in the sales department had overcharged Remy. If the cost of a piece of furniture is $134, how much money will Sally’s Woodworking LLC reimburse Remy?"""
    # Define the original total amount paid by Remy and the cost of a single piece of furniture
    total_paid = 20700
    cost_per_piece = 134

    # Calculate the actual total cost of the furniture
    actual_total_cost = 150 * cost_per_piece

    # Calculate the overcharge
    overcharge = total_paid - actual_total_cost

    # Return the amount to be reimbursed to Remy
    result = overcharge
    return result

print(solution())