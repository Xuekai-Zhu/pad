def solution():
    # Define the total distance Arvin wants to run in a week
    total_distance = 20

    # Define Arvin's initial distance on the first day
    first_day_distance = 2

    # Define the number of subsequent days Arvin runs
    subsequent_days = 4

    # Calculate the total distance Arvin runs on the subsequent days
    subsequent_distance = sum(range(first_day_distance+1, first_day_distance+1+subsequent_days))

    # Calculate the total distance Arvin runs in a week
    weekly_distance = first_day_distance + subsequent_distance

    # Calculate the distance Arvin runs on the 5th day
    fifth_day_distance = weekly_distance - sum(range(1,5))

    result = fifth_day_distance
    return result

print(solution())