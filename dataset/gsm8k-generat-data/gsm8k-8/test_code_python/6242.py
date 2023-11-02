def solution():
    # Define the amount of water Tim drinks each day
    daily_amount = 2 * 1.5 * 32 + 20  # Convert quarts to ounces

    # Calculate the amount of water Tim drinks in a week
    weekly_amount = daily_amount * 7

    # Convert weekly amount back to quarts
    weekly_amount = weekly_amount / 32

    result = weekly_amount
    return result

print(solution())