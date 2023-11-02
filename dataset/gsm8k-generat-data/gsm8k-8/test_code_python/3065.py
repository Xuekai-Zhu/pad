def solution():
    # Define the initial weight Tom can lift
    initial_weight = 80

    # Double the weight after training
    doubled_weight = initial_weight * 2

    # Add 10% extra weight after specializing
    specialized_weight = doubled_weight * 1.1

    # Calculate the total weight Tom can hold
    total_weight = specialized_weight * 2
    result = total_weight
    return result

print(solution())