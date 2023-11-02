def solution():
    hourly_rate = 50.0
    hours_worked = 10.0
    late_penalty = 0.2  # 20% penalty for being late

    # Calculate the total amount earned without penalties
    total_earned_no_penalty = hourly_rate * hours_worked

    # Calculate the amount of the penalty
    penalty_amount = total_earned_no_penalty * late_penalty

    # Calculate the final amount earned after the penalty is applied
    final_amount_earned = total_earned_no_penalty - penalty_amount
    result = final_amount_earned
    return result

print(solution())