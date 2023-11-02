def solution():
    """Sol sells candy bars to raise money for her softball team. On the first day, she sells ten candy bars and sells four more candy bars than she sold the previous day each day afterward. If she sells six days a week and each candy bar costs 10 cents, how much will she earn in a week in dollars?"""
    
    # Define the number of candy bars Sol sells on the first day
    first_day_sales = 10

    # Define the number of additional candy bars Sol sells each day
    additional_sales = 4

    # Define the number of days Sol sells candy bars
    num_days = 6

    # Calculate the total number of candy bars sold in the week
    total_sales = first_day_sales
    for i in range(1, num_days):
        total_sales += first_day_sales + i*additional_sales

    # Calculate the total earnings from candy bar sales
    earnings = total_sales * 0.1

    # Display the earnings in dollars
    result = earnings
    return result

print(solution())