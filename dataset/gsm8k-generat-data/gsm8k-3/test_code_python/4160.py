def solution():
    """Hannah harvests 5 strawberries daily for the next whole month of April, which has 30 days. If she gives away 20 strawberries to her friends and 30 strawberries are stolen, how many strawberries does she have by the end of April?"""
    # Define the number of strawberries harvested daily
    STRAWBERRIES_DAILY = 5

    # Calculate the total number of strawberries harvested in April
    total_strawberries = STRAWBERRIES_DAILY * 30

    # Subtract the number of strawberries given away and stolen
    total_strawberries -= 20
    total_strawberries -= 30

    # Display the remaining number of strawberries
    result = total_strawberries
    return result

print(solution())