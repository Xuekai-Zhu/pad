def solution():
    
    april_september_months = 6
    october_march_months = 6
    april_september_cuts = 15 * april_september_months
    october_march_cuts = 3 * october_march_months
    total_cuts = april_september_cuts + october_march_cuts
    average_cuts_per_month = total_cuts / 12
    result = average_cuts_per_month
    return result

print(solution())