def solution():
    """Gail has some bills in her wallet which amount to $100. She has four $5 bills and three $20 bills, and the rest are $10 bills. How many $10 bills are in her wallet?"""
    total_amount = 100
    five_bills = 4
    twenty_bills = 3
    total_five_bills = five_bills * 5
    total_twenty_bills = twenty_bills * 20
    total_other_bills = total_amount - total_five_bills - total_twenty_bills
    num_ten_bills = total_other_bills / 10
    result = num_ten_bills
    return result

print(solution())