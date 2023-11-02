def solution():
    # Calculate the fees for the first week
    first_week_fee = 100 * 0.05  # finance fee is 5% of the amount borrowed

    # Calculate the fees for the second week
    second_week_fee = 100 * 0.1  # finance fee is now doubled to 10%

    # Calculate the total fees for 2 weeks
    total_fee = first_week_fee + second_week_fee

    result = total_fee
    return result

print(solution())