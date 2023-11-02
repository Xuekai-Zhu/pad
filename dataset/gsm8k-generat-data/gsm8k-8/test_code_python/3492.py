def solution():
    # Calculate the total amount of money from the $5 and $20 bills
    total_money = 150 - (50 + (4 * 20))

    # Calculate the number of $5 bills
    num_5 = total_money // 5

    # Calculate the number of $10 bills
    num_10 = 50

    # Calculate the total number of bills
    total_bills = num_5 + num_10 + 4
    
    result = total_bills
    return result

print(solution())