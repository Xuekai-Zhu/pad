def solution():
    """James took a job delivering groceries in his neighborhood. He can carry 10 bags on each trip. If he takes 20 trips a day, how many bags does he deliver in 5 days?"""
    # Define the number of bags James can carry on each trip
    BAGS_PER_TRIP = 10

    # Define the number of trips James takes each day
    TRIPS_PER_DAY = 20

    # Define the number of days James works
    DAYS_WORKED = 5

    # Calculate the total number of bags James delivers
    total_bags = BAGS_PER_TRIP * TRIPS_PER_DAY * DAYS_WORKED

    # Display the total number of bags
    result = total_bags
    return result

print(solution())