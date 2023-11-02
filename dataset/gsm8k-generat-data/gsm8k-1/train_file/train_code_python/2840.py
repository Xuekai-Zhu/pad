def solution():
    """Dolly wants to ride the Ferris wheel twice, the roller coaster three times, and the log ride seven times. The Ferris wheel costs 2 tickets, the roller coaster costs 5 tickets and the log ride costs 1 ticket. Dolly has 20 tickets. How many more tickets should Dolly buy?"""
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