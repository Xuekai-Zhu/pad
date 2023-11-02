def solution():
    total_us_states = 50
    num_collected_states = 40
    percentage_collected = num_collected_states / total_us_states * 100

    # Calculate the amount earned from Paul's parents
    amount_earned = percentage_collected * 2
    result = amount_earned
    return result

print(solution())