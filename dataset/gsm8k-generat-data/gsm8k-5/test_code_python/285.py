def solution():
    total_episodes = 20
    episode_length = 30  # Each episode is 30 minutes long
    total_length = total_episodes * episode_length  # Calculate the total length of the show in minutes

    total_days = 5  # John wants to finish the show in 5 days
    total_hours = total_days * 24  # Convert the total number of days to hours

    hours_per_day = total_length / (total_hours * 60)  # Divide the total length by the total available time in hours
    
    result = hours_per_day
    return result

print(solution())