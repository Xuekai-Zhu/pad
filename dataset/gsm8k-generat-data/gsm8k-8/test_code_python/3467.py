def solution():
    # Define variables
    bills_given = 25 - 15 + 1 # includes his 15th birthday and his 25th birthday
    bills_spent = 0.2 * bills_given
    bills_left = bills_given - bills_spent
    exchange_rate = 1.5

    # Calculate the amount he will receive from his parents
    amount_received = bills_left * exchange_rate
    result = amount_received
    return result

print(solution())