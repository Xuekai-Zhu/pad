def solution():
    
    hourly_rate = 10
    num_colleges = 6
    app_fee = 25
    total_fee = num_colleges * app_fee
    hours_needed = total_fee / hourly_rate
    result = hours_needed
    return result

print(solution())