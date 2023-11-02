def solution():
    """Tye goes to two different banks and withdraws $300 from each bank. If he got it all in 20 dollar bills how many bills did he get?"""
    # Define the amount to withdraw from each bank
    amount = 300

    # Calculate the number of 20 dollar bills from each bank
    bills_per_bank = amount // 20

    # Calculate the total number of 20 dollar bills
    total_bills = bills_per_bank * 2

    result = total_bills
    return result

print(solution())