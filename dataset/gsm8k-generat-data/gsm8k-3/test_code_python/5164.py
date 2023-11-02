def solution():
    """Tye goes to two different banks and withdraws $300 from each bank.  If he got it all in 20 dollar bills how many bills did he get?"""
    # Calculate the total amount of money Tye withdrew
    total_withdrawal = 300 * 2

    # Calculate the number of 20 dollar bills Tye received
    num_bills = total_withdrawal // 20

    # Display the number of bills Tye received
    result = num_bills
    return result

print(solution())