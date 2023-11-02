def solution():
    
    num_kinder = 26
    num_first = 19
    num_second = 20
    num_third = 25
    time_per_check = 2
    total_time = (num_kinder + num_first + num_second + num_third) * time_per_check
    hours = total_time / 60
    result = hours
    return result

print(solution())