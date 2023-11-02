def solution():
    # Define the total number of wood bundles used during the day
    total_used = 10 - 3

    # Define the number of wood bundles used in the morning
    morning_used = 4

    # Calculate the number of wood bundles used in the afternoon
    afternoon_used = total_used - morning_used

    result = afternoon_used
    return result

print(solution())