def solution():
    """Hannah harvests 5 strawberries daily for the next whole month of April, which has 30 days. If she gives away 20 strawberries to her friends and 30 strawberries are stolen, how many strawberries does she have by the end of April?"""
    # Define the number of days in April
    days = 30

    # Calculate the total number of strawberries harvested
    total_strawberries = 5 * days

    # Subtract the strawberries given away and stolen
    remaining_strawberries = total_strawberries - 20 - 30
    
    result = remaining_strawberries
    return result

print(solution())