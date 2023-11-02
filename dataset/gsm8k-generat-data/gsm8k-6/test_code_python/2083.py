def solution():
    # Calculate the cost of pistachios per ounce
    cost_per_ounce = 10 / 5  # $10 per can, each can is 5 ounces

    # Calculate the cost of pistachios eaten in 5 days
    cost_per_5_days = cost_per_ounce * 30  # 30 ounces of pistachios eaten every 5 days

    # Calculate the cost of pistachios per week
    cost_per_week = cost_per_5_days * 7 / 5  # 7 days in a week
    result = cost_per_week
    return result

print(solution())