def solution():
    episode_length = 20  # Each episode is 20 minutes long
    filming_time = episode_length * 1.5  # It takes 50% longer than the episode duration to film each episode
    episodes_per_week = 5  # They film 5 episodes per week
    weeks = 4  # They want to film 4 weeks of episodes

    # Calculate the total filming time for 4 weeks of episodes
    total_filming_time = (episode_length + filming_time) * episodes_per_week * weeks

    # Convert the total filming time to hours
    filming_hours = total_filming_time / 60
    result = filming_hours
    return result

print(solution())