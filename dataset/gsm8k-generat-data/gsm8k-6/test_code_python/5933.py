def solution():
    # Calculate the total amount of money Marly has in dollars
    total_money = 10 * 20 + 8 * 10 + 4 * 5  # 10 $20 bills, 8 $10 bills, and 4 $5 bills
    # Calculate the number of $100 bills she will have after the change
    num_hundred_bills = total_money // 100
    result = num_hundred_bills
    return result

print(solution())