def solution():
    
    initial_elephants = 30000
    exiting_rate = 2880
    exiting_time = 4
    exiting_amount = exiting_rate * exiting_time
    remaining_elephants = initial_elephants - exiting_amount
    final_elephants = 28980
    entering_time = 7
    entering_amount = final_elephants - remaining_elephants
    entering_rate = entering_amount / entering_time
    result = entering_rate
    return result

print(solution())