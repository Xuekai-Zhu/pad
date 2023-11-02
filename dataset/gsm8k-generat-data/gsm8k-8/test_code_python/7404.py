def solution():
    # Define the fee for the first 5 days
    fee_first_5_days = 100 * 5

    # Define the fee for the remaining days
    fee_remaining_days = 60 * 5

    # Calculate the total fee
    total_fee = fee_first_5_days + fee_remaining_days

    # Return the total fee
    return total_fee

print(solution())