def solution():
    """John wants to finish a show in 5 days. There are 20 episodes and they are each 30 minutes long. How many hours does he have to watch a day?"""
    
    # Define the number of episodes and length of each episode
    num_episodes = 20
    episode_length = 30 # in minutes
    
    # Convert episode length from minutes to hours
    episode_length_hours = episode_length / 60
    
    # Total time needed to finish the show in hours
    total_time_hours = num_episodes * episode_length_hours
    
    # Number of hours John needs to watch per day to finish the show in 5 days
    hours_per_day = total_time_hours / 5
    
    # Round to 2 decimal places
    hours_per_day = round(hours_per_day, 2)
    
    # Return the result
    result = hours_per_day
    return result

print(solution())