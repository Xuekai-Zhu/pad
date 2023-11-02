def solution():
    num_bills_given = 10   # George was given 1 bill each year from his 15th to 24th birthday
    num_bills_remaining = int(num_bills_given * 0.8)   # George spent 20% of his bills

    exchange_rate = 1.5
    total_money_received = num_bills_remaining * exchange_rate
    result = total_money_received
    return result

print(solution())