def solution():
    
    total_bottles = 24
    first_day_percent = 1/3
    first_day_consumed = total_bottles * first_day_percent
    remaining_bottles = total_bottles - first_day_consumed
    second_day_percent = 1/2
    second_day_consumed = remaining_bottles * second_day_percent
    remaining_bottles -= second_day_consumed
    result = remaining_bottles
    return result

print(solution())