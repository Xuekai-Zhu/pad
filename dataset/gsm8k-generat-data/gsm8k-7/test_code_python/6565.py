def solution():
    flat_rate = 20
    rate_per_minute = 7
    total_amount_paid = 146

    # Calculate the amount paid for the minutes only
    amount_paid_for_minutes = total_amount_paid - flat_rate

    # Calculate the number of minutes tutored
    num_minutes = amount_paid_for_minutes / rate_per_minute

    result = num_minutes
    return result

print(solution())