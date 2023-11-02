def solution():
    """Gail has some bills in her wallet which amount to $100. She has four $5 bills and three $20 bills, and the rest are $10 bills. How many $10 bills are in her wallet?"""
    total_amount = 100
    five_bill_amount = 4 * 5
    twenty_bill_amount = 3 * 20
    remaining_amount = total_amount - five_bill_amount - twenty_bill_amount
    ten_bill_count = remaining_amount / 10
    result = ten_bill_count
    return result

print(solution())