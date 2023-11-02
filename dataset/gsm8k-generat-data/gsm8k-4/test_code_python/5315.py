def solution():
    """Sam went for a run in the morning. In the afternoon, he went grocery shopping and walked twice the distance through the store as he had run that morning. That evening, he went on a bike ride with his family and biked for 12 miles. In all, he went 18 miles that day. How many miles was Sam’s morning run?"""
    # Define the distance walked in the afternoon as a function of the distance of the morning run
    def distance_walked(morning_run):
        return morning_run * 2

    # Define the equation for the total distance traveled that day
    def total_distance(morning_run):
        return morning_run + distance_walked(morning_run) + 12

    # Use a loop to find the morning run distance that results in a total distance of 18 miles
    for i in range(1, 18):
        if total_distance(i) == 18:
            result = i
            break

    return result

print(solution())