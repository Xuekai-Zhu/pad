def solution():
    percent_trips = 40
    percent_drops = 25
    percent_not_dropping = 100 - percent_drops
    result = percent_trips * percent_not_dropping
    
    return result

print(solution())