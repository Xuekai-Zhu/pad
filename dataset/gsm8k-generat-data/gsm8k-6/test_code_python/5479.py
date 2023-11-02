def solution():
    # Calculate the total cost of the drill bits
    total_cost = 5 * 6  # 5 sets of drill bits, each set costs 6 dollars
    tax = total_cost * 0.1  # 10% tax on the order
    total_paid = total_cost + tax
    
    result = total_paid
    return result

print(solution())