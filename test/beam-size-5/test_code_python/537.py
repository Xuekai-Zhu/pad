def solution():
    target_amount = 1125  # Elvis has a monthly saving target of $1125
    first_half_amount = target_amount / 2  # Elvis wants to save twice as much daily in the first half in April
    second_half_amount = first_half_amount * 2  # Elvis wants to save twice as much daily in the second half in April

    # Calculate the amount Elvis needs to save per day in the second half of the month
    savings_per_day = second_half_amount / 2
    result = savings_per_day
    return result

print(solution())