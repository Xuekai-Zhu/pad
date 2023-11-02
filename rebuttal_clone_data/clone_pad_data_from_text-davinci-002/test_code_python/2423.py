def solution():
    initial_amount = 100
    flow_rate = 2
    duration = 90
    total_rainfall = flow_rate * duration
    final_amount = initial_amount + total_rainfall
    result = final_amount
    return result

print(solution())