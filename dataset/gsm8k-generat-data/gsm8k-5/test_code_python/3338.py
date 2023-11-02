def solution():
    time_waiting_for_number = 20  # Nicky spent 20 minutes waiting to take a number
    time_waiting_for_called_number = time_waiting_for_number * 4 + 14  # Nicky waited 4 times longer than taking a number, plus 14 minutes
    total_waiting_time = time_waiting_for_number + time_waiting_for_called_number  # Add the two wait times together

    result = total_waiting_time
    return result

print(solution())