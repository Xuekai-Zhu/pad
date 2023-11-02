def solution():
    """Sam went for a run in the morning. In the afternoon, he went grocery shopping and walked twice the distance through the store as he had run that morning. That evening, he went on a bike ride with his family and biked for 12 miles. In all, he went 18 miles that day. How many miles was Sam’s morning run?"""
    
    # Define the distance Sam walked through the store
    store_distance = 0

    # Define the distance of Sam's bike ride
    bike_distance = 12

    # Set a variable to represent the distance of Sam's morning run
    morning_run_distance = 0

    # Loop through possible values for the morning run distance and check if it leads to the total distance being 18 miles
    for i in range(18):
        morning_run_distance = i
        afternoon_walk_distance = morning_run_distance * 2
        total_distance = morning_run_distance + afternoon_walk_distance + bike_distance
        if total_distance == 18:
            break

    # Display the distance of Sam's morning run
    result = morning_run_distance
    return result

print(solution())