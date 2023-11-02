def solution():
    
    fw_rides = 2
    rc_rides = 3
    lr_rides = 7
    fw_cost = 2
    rc_cost = 5
    lr_cost = 1
    total_cost = fw_rides * fw_cost + rc_rides * rc_cost + lr_rides * lr_cost
    tickets_needed = total_cost - 20
    result = tickets_needed
    return result

print(solution())