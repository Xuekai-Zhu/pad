def solution():
    # Calculate the amount spent on Monday
    spent_on_monday = 200 / 2

    # Calculate the remainder
    remainder = 200 - spent_on_monday

    # Calculate the amount spent on Tuesday
    spent_on_tuesday = remainder / 4

    # Calculate the remaining balance
    remaining_balance = remainder - spent_on_tuesday

    result = remaining_balance
    return result

print(solution())