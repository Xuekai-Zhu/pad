def solution():
    # Define Jack's initial amount
    initial_amount = 43

    # Define Jack's allowance per week
    allowance_per_week = 10

    # Calculate the total amount Jack will add to his piggy bank over 8 weeks
    total_addition = (allowance_per_week / 2) * 8

    # Calculate Jack's final amount in his piggy bank
    final_amount = initial_amount + total_addition

    result = final_amount
    return result

print(solution())