def solution():
    """In preparation for his mountain climbing, Arvin wants to run a total of 20 kilometers in a week. On the first day, he ran 2 kilometers. On each subsequent day, he increased his running distance by 1 kilometer over the previous day. If he runs for 5 days a week, how many kilometers did he run on the 5th day?"""
    # Define the total distance Arvin wants to run and the distance he ran on the first day
    total_distance = 20
    first_day_distance = 2

    # Calculate the total distance Arvin ran on the remaining 4 days
    remaining_distance = total_distance - first_day_distance
    daily_increase = 1
    total_days = 4
    total_remaining_increase = daily_increase * total_days
    remaining_distance -= total_remaining_increase

    # Calculate the distance Arvin ran on the 5th day
    fifth_day_distance = remaining_distance // 5

    # Display the distance Arvin ran on the 5th day
    result = fifth_day_distance
    return result

print(solution())