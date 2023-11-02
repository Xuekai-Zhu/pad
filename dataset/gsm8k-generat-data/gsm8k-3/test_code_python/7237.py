def solution():
    """Jack has $43 in his piggy bank. He also gets an allowance of $10 a week. If Jack puts half of his allowance into his piggy bank every week, after 8 weeks how much will Jack have in his piggy bank?"""
    # Define the initial amount in Jack's piggy bank and his weekly allowance
    piggy_bank = 43
    weekly_allowance = 10

    # Calculate the amount Jack puts into his piggy bank each week
    piggy_bank_deposit = weekly_allowance / 2

    # Calculate the total amount Jack will have in his piggy bank after 8 weeks
    total_piggy_bank = piggy_bank + (piggy_bank_deposit * 8)

    # Display the total amount in Jack's piggy bank
    result = total_piggy_bank
    return result

print(solution())