def solution():
    amount_received = 200  # Smith gave Randy $200
    amount_given_away = 1200  # Randy gave Sally $1200
    amount_remaining = 2000  # Randy has $2000 left

    # Calculate the total amount Randy had at first
    total_amount = amount_received + amount_given_away + amount_remaining
    result = total_amount
    return result

print(solution())