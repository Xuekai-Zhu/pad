def solution():
    # Calculate the total amount of dog food consumed by both dogs in a day
    daily_consumption = 2 * 6 * 1/4  # 2 dogs, 6 cups each, 1/4 pound per cup

    # Calculate the monthly consumption
    monthly_consumption = daily_consumption * 30  # Assuming 30 days in a month

    # Calculate the number of 20-pound bags required
    bags_required = monthly_consumption / 20

    result = bags_required
    return result

print(solution())