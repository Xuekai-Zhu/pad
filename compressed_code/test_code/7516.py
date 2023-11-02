def solution():
    
    peak_hours = [11, 12, 13, 17, 18]
    serving_rate_peak = 12
    serving_rate_off_peak = 8
    total_customers_peak = 0
    total_customers_off_peak = 0
    for hour in range(16, 18):
        if hour in peak_hours:
            total_customers_peak += (serving_rate_peak * 4)
        else:
            total_customers_off_peak += (serving_rate_off_peak * 4)
    total_customers = total_customers_peak + total_customers_off_peak
    result = total_customers
    return result

print(solution())