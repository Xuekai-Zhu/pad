def solution():
    
    start_amount = 10
    target_month = 5
    current_amount = start_amount
    for i in range(2, target_month + 1):
        current_amount *= 2

    result = current_amount
    return result

print(solution())