def solution():
    # Calculate the total number of customers served during peak hours
    peak_customers = 12 * 8  # 12 cars every 15 minutes for 2 hours (11 am-1 pm), and 5 pm-6 pm is 1 hour
    # Calculate the total number of customers served during off-peak hours
    off_peak_customers = 8 * 8   # 8 cars every 15 minutes for 2 hours (4 pm-6 pm)
    # Calculate the total number of customers served during 4 pm-6 pm
    total_customers = peak_customers + off_peak_customers
    result = total_customers
    return result

print(solution())