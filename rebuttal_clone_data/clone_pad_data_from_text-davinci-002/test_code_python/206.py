def solution():
    """There are some lions in Londolozi at first. Lion cubs are born at the rate of 5 per month and lions die at the rate of 1 per month. If there are 148 lions in Londolozi after 1 year, how many lions were there in Londolozi at first?"""
    birth_rate = 5
    death_rate = 1
    total_lions_after_1_year = 148
    total_lions_at_first = total_lions_after_1_year / ((birth_rate - death_rate) / 12 + 1)
    result = total_lions_at_first
    return result

print(solution())