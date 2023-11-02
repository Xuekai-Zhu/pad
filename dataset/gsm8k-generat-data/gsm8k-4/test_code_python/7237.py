def solution():
    """Jack has $43 in his piggy bank. He also gets an allowance of $10 a week. If Jack puts half of his allowance into his piggy bank every week, after 8 weeks how much will Jack have in his piggy bank?"""
    # Define the initial amount in Jack's piggy bank and his weekly allowance
    piggy_bank_amount = 43
    weekly_allowance = 10

    # Calculate the amount Jack puts into his piggy bank each week
    amount_saved_per_week = weekly_allowance / 2

    # Calculate the total amount Jack will save after 8 weeks
    total_saved = piggy_bank_amount + (amount_saved_per_week * 8)

    result = total_saved
    return result

print(solution())