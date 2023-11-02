def solution():
    current_temp = 84
    decrease_ratio = 3/4
    decrease_amount = current_temp * (1 - decrease_ratio)
    result = decrease_amount
    return result

print(solution())