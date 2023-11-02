def solution():
    # Define yesterday's water intake
    yesterday_intake = 48

    # Calculate the percentage of decrease from two days ago to yesterday
    decrease_percentage = 4 / 100

    # Calculate yesterday's water intake as a percentage of two days ago's intake
    yesterday_percentage = 1 - decrease_percentage
    two_days_ago_intake = yesterday_intake / yesterday_percentage

    result = two_days_ago_intake
    return result

print(solution())