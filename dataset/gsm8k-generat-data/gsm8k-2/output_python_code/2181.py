def solution():
    """At peak hours, 11 am - 1 pm and 5 pm - 6 pm, the local fast-food restaurant serves 12 cars every 15 minutes. Off-peak times, they serve 8 cars every 15 minutes. From 4 pm - 6 pm, how many customers do they serve?"""
    peak_hours_customers = 12 * 4  # 11 am - 1 pm and 5 pm - 6 pm, 2 hours total
    off_peak_customers = 8 * 8  # 4 pm - 5 pm, 1 hour total
    total_customers = peak_hours_customers + off_peak_customers
    result = total_customers
    return result

print(solution())