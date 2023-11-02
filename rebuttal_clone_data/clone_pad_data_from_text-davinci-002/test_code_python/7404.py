def solution():
    initial_fee = 100
    subsequent_fee = 60
    days_searched = 10
    total_fee = initial_fee + (days_searched - 5) * subsequent_fee
    result = total_fee
    return result

print(solution())