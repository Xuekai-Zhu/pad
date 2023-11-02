def solution():
    
    hours_2_to_4 = 2
    hours_4_to_7 = 3
    hours_7_to_9 = 2
    rate_2_to_4 = 4
    rate_4_to_7 = 3
    rate_7_to_9 = 0.5
    starting_amount = 2
    total_amount = starting_amount + (hours_2_to_4 * rate_2_to_4) + (hours_4_to_7 * rate_4_to_7) + (hours_7_to_9 * rate_7_to_9)
    result = total_amount
    return result

print(solution())