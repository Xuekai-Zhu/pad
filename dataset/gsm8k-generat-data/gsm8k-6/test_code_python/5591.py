def solution():
    # Calculate how many days it will take for Chris to reach 90 seconds
    total_hold_time = 0  
    days = 0  
    while total_hold_time < 90:
        days += 1
        total_hold_time += 10 * days  
    result = days
    return result

print(solution())