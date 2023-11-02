def solution():
    # Define the amount of shampoo used daily
    shampoo_daily = 1

    # Calculate the amount of conditioner used daily
    conditioner_daily = 0.5 * shampoo_daily

    # Calculate the total amount of shampoo and conditioner used in 2 weeks (14 days)
    total_daily_usage = shampoo_daily + conditioner_daily
    total_usage = 14 * total_daily_usage

    result = total_usage
    return result

print(solution())