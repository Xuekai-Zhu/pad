def solution():
    """Tim buys 3 loaves of bread.  Each loaf of bread has 20 slices.  He pays for the 3 loaves of bread with 2 $20 bills.  He gets $16 change.  How much does each slice cost, in cents?"""
    # Calculate the total cost of the bread
    total_cost = 3 * 20 * 100  # 3 loaves * 20 slices * 100 cents

    # Calculate the amount paid by Tim
    amount_paid = 2 * 20 * 100  # 2 $20 bills * 100 cents per dollar

    # Calculate the amount of change given to Tim
    change = 16 * 100  # $16 change * 100 cents per dollar

    # Calculate the cost per slice of bread, in cents
    cost_per_slice = (total_cost - amount_paid + change) / (3 * 20)

    # Display the cost per slice of bread, in cents
    result = cost_per_slice
    return result

print(solution())