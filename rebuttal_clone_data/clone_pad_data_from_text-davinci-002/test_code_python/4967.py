def solution():
    max_capacity = 350000
    initial_loss = 32000
    final_loss = 10000
    initial_repair_attempt = 5
    final_repair_attempt = 10
    repair_success_rate = 40
    tank_remaining_capacity = max_capacity - (initial_loss * initial_repair_attempt) - (final_loss * final_repair_attempt) 
    time_to_fill = (max_capacity - tank_remaining_capacity) / repair_success_rate
    result = time_to_fill
    return result

print(solution())