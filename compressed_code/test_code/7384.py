def solution():
    
    oysters_per_5min = 10
    minutes_in_2hrs = 120
    oysters_per_2hrs = oysters_per_5min * (minutes_in_2hrs / 5)
    result = oysters_per_2hrs
    return result

print(solution())