def solution():
    # Calculate the total amount of money from the $5 and $20 bills
    total_money = (4 * 5) + (3 * 20)  # four $5 bills and three $20 bills
    
    # Calculate the amount of money from the $10 bills
    remaining_money = 100 - total_money
    
    # Calculate the number of $10 bills based on the remaining money
    num_10_bills = remaining_money // 10
    
    result = num_10_bills
    return result

print(solution())