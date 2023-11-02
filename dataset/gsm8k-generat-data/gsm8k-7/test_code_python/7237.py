def solution():
    initial_amount = 43
    weekly_allowance = 10
    num_weeks = 8

    # Calculate the total amount Jack will get from his weekly allowance in 8 weeks
    total_allowance = weekly_allowance * num_weeks

    # Calculate the total amount Jack will put into his piggy bank from his weekly allowance in 8 weeks
    total_saved = (weekly_allowance / 2) * num_weeks

    # Calculate the total amount Jack will have in his piggy bank after 8 weeks
    total_amount = initial_amount + total_saved

    result = total_amount
    return result

print(solution())