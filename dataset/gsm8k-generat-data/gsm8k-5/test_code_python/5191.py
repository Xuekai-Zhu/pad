def solution():
    total_states = 50  # There are 50 states in the US
    num_states_collected = 40  # Paul has collected plates from 40 different states

    # Calculate the percentage of total states Paul has collected plates from
    percentage_collected = (num_states_collected / total_states) * 100

    # Calculate the amount earned from Paul's parents
    earnings = percentage_collected * 2
    result = earnings
    return result

print(solution())