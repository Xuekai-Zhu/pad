def solution():
    """Samuel has $5, $10, and $20 bills which amount to $150 in his wallet. His $10-bills amount to $50, and he has 4 $20-bills. How many bills does Samuel have in his wallet?"""
    total_amount = 150
    num_ten_bills = 5
    ten_bills_amount = 50
    num_twenty_bills = 4
    remaining_amount = total_amount - (num_ten_bills * 10) - (num_twenty_bills * 20) - ten_bills_amount
    num_five_bills = remaining_amount / 5
    total_bills = num_ten_bills + num_twenty_bills + num_five_bills
    result = total_bills
    return result

print(solution())