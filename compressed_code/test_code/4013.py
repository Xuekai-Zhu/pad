def solution():
    
    total_homes = 200
    homes_delivered_first_hour = total_homes * (2/5)
    homes_remaining_after_first_hour = total_homes - homes_delivered_first_hour
    homes_delivered_second_hour = homes_remaining_after_first_hour * 0.6
    homes_remaining = total_homes - homes_delivered_first_hour - homes_delivered_second_hour
    result = homes_remaining
    return result

print(solution())