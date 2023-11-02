def solution():
    """There are some lions in Londolozi at first. Lion cubs are born at the rate of 5 per month and lions die at the rate of 1 per month. If there are 148 lions in Londolozi after 1 year, how many lions were there in Londolozi at first?"""
    current_lions = 148
    born_rate = 5
    death_rate = 1
    time_in_months = 12
    new_lions = born_rate - death_rate
    original_lions = (current_lions - (new_lions * time_in_months)) / (1 - new_lions)
    result = original_lions
    return result

print(solution())