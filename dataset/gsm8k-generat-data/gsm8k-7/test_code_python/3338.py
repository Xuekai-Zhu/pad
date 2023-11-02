def solution():
    time_waiting_to_take_number = 20
    time_waiting_for_number_to_be_called = 4*time_waiting_to_take_number + 14
    
    total_time_waiting = time_waiting_to_take_number + time_waiting_for_number_to_be_called
    result = total_time_waiting
    return result

print(solution())