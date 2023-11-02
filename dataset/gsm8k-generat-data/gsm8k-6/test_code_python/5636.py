def solution():
    # Calculate the total cost of Dakota and Ben's original order
    total_cost = 2*3 + 2*2 + 2*2  # eggs, pancakes, and 2 mugs of cocoa
    total_cost += 1  # tax
    # Add Ben's additional order
    total_cost += 2 + 2  # 1 batch of pancakes and 1 mug of cocoa
    # Calculate the change from $15
    change = 15 - total_cost
    result = change
    return result

print(solution())