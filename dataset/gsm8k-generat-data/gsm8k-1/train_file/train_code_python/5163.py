def solution():
    """Tye goes to two different banks and withdraws $300 from each bank. If he got it all in 20 dollar bills how many bills did he get?"""
    amount_per_bank = 300
    denomination = 20
    bills_per_bank = amount_per_bank / denomination
    total_bills = bills_per_bank * 2
    result = total_bills
    return result

print(solution())