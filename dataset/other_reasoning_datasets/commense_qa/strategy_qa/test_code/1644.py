def solution():
    pandemic_month = "June"
    large_events_banned = True
    parc_des_princes_operational = False
    if pandemic_month == "June" and not large_events_banned and parc_des_princes_operational:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())