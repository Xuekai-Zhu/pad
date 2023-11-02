def solution():
    # Calculate the total amount earned by Cherry in a week
    amount_earned_per_day = (4 * 2.5) + (2 * 4)  # four 5 kg cargos and two 8 kg cargos per day
    total_amount_earned = amount_earned_per_day * 7  # multiply by 7 days in a week
    result = total_amount_earned
    return result

print(solution())