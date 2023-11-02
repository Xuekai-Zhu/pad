def solution():
    money_earned = 10
    money_per_hour = 10
    weeds_picked = money_earned * 100
    time_taken = weeds_picked / money_per_hour * 3600
    seconds_per_weed = time_taken / weeds_picked
    result = seconds_per_weed
    return result

print(solution())