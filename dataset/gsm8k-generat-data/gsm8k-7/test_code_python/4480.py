def solution():
    rate1 = 2  # ounces of cleaner per minute for first 15 minutes
    rate2 = 3  # ounces of cleaner per minute for next 10 minutes
    rate3 = 4  # ounces of cleaner per minute for the final 5 minutes
    time1 = 15  # minutes at rate1
    time2 = 10  # minutes at rate2
    time3 = 5  # minutes at rate3

    # Calculate the total amount of cleaner used during each time period
    amount1 = rate1 * time1
    amount2 = rate2 * time2
    amount3 = rate3 * time3

    # Calculate the total amount of cleaner used in 30 minutes
    total_amount = amount1 + amount2 + amount3
    result = total_amount
    return result

print(solution())