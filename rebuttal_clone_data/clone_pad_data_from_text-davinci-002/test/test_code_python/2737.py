def solution():
    time_spent_on_first_step = 30
    time_spent_on_second_step = time_spent_on_first_step / 2
    time_spent_on_third_step = time_spent_on_first_step + time_spent_on_second_step
    total_time_spent = time_spent_on_first_step + time_spent_on_second_step + time_spent_on_third_step
    result = total_time_spent
    return result

print(solution())