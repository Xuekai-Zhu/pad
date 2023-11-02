def solution():
    # Define the amount collected in two weeks
    collected_in_2_weeks = 280

    # Calculate the total collected after three weeks
    collected_in_3_weeks = collected_in_2_weeks * 6

    # Calculate the amount needed in the third week to reach the target
    amount_needed_in_3rd_week = collected_in_2_weeks * 6 + 320 - collected_in_3_weeks

    # Calculate the target amount
    target_amount = collected_in_2_weeks * 6 + amount_needed_in_3rd_week

    result = target_amount
    return result

print(solution())