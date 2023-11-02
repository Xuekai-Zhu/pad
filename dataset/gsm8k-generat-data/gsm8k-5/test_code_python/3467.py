def solution():
    num_bills = 25 - 15 + 1  # George has been given a special bill each year from his 15th to 25th birthday

    # Calculate the number of bills he still has after spending 20%
    num_bills_remaining = int(num_bills * 0.8)

    # Calculate the amount he will receive from his parents when he exchanges the bills
    amount_received = num_bills_remaining * 1.5

    result = amount_received
    return result

print(solution())