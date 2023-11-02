def solution():
    # Calculate the total amount of money Tye withdrew
    total_withdraw = 300 * 2  # he withdraws $300 from each of the two banks
    # Calculate the number of $20 bills Tye received
    num_bills = total_withdraw / 20  # each bill is worth $20
    result = num_bills
    return result

print(solution())