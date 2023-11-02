def solution():
    # Define the time Nicky spent waiting to take a number and to have his number called
    waiting_for_number = 20
    waiting_for_call = 4 * waiting_for_number + 14

    # Calculate the total waiting time
    total_waiting_time = waiting_for_number + waiting_for_call
    result = total_waiting_time
    return result

print(solution())