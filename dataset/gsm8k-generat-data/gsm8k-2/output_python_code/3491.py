def solution():
    """Samuel has $5, $10, and $20 bills which amount to $150 in his wallet. His $10-bills amount to $50, and he has 4 $20-bills. How many bills does Samuel have in his wallet?"""
    total_money = 150
    num_10_bills = 5
    num_20_bills = 4
    total_10_bills = num_10_bills * 10
    total_20_bills = num_20_bills * 20
    total_5_bills = total_money - total_10_bills - total_20_bills
    num_5_bills = total_5_bills // 5
    total_bills = num_5_bills + num_10_bills + num_20_bills
    result = total_bills
    return result

print(solution())