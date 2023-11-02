def solution():
    """Oscar wants to train for a marathon. He plans to add 2/3 of a mile each week until he reaches a 20-mile run. How many weeks before the marathon should he start training if he has already run 2 miles?"""
    # Define the starting distance and the target distance
    starting_distance = 2
    target_distance = 20

    # Define the weekly distance increase
    weekly_increase = 2/3

    # Calculate the number of weeks needed to reach the target distance
    distance_to_cover = target_distance - starting_distance
    weeks_needed = int(distance_to_cover / weekly_increase)

    # Display the number of weeks needed
    result = weeks_needed
    return result

print(solution())