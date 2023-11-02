def solution():
    # Calculate Dino's earnings from his gig work
    earnings = (20*10) + (30*20) + (5*40)  # Dino works 20 hours at $10 per hour, 30 hours at $20 per hour, and 5 hours at $40 per hour

    # Calculate Dino's net income after paying expenses
    net_income = earnings - 500  # Dino pays $500 in expenses

    result = net_income
    return result

print(solution())