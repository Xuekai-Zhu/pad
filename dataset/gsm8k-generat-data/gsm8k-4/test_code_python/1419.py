def solution():
    """In preparation for his mountain climbing, Arvin wants to run a total of 20 kilometers in a week. On the first day, he ran 2 kilometers. On each subsequent day, he increased his running distance by 1 kilometer over the previous day. If he runs for 5 days a week, how many kilometers did he run on the 5th day?"""
    # Define the total distance Arvin wants to run in a week
    total_distance = 20

    # Define the starting distance on the first day
    first_day_distance = 2

    # Define the number of days Arvin runs in a week
    num_days = 5

    # Calculate the total distance Arvin runs in the remaining 4 days
    remaining_distance = total_distance - first_day_distance

    # Calculate the increase in distance per day
    increase = 1

    # Calculate the distance Arvin runs on the 5th day
    fifth_day_distance = first_day_distance + increase * (num_days - 1)

    # return the result
    result = fifth_day_distance
    return result

print(solution())