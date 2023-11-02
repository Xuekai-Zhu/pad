def solution():
    """If the wages of 15 workers for 6 days is $9450. What would be the wages for 19 workers for 5 days?"""
    # calculate the daily wage for each worker
    wage_per_worker = 9450 / (15 * 6)
    
    # calculate the wages for 19 workers for 5 days
    total_wages = wage_per_worker * (19 * 5)
    
    result = total_wages
    return result

print(solution())