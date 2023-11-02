def solution():
    """There are 100 lions in Londolozi at first. If lion cubs are born at the rate of 5 per month and lions die at the rate of 1 per month, how many lions will there be in Londolozi after 1 year?"""
    lion_count = 100
    birth_rate = 5
    death_rate = 1
    for i in range(12): # 12 months in a year
        lion_count = lion_count + birth_rate - death_rate
    result = lion_count
    return result

print(solution())