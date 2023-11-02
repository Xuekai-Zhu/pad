def solution():
    
    worker_pay = 10
    worker_1_hours = 10
    worker_2_hours = 8 + 15
    total_hours = worker_1_hours + worker_2_hours
    total_pay = total_hours * worker_pay * 2
    result = total_pay
    return result

print(solution())