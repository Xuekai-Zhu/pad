def solution():
    # Define the total number of episodes Marc bought
    total_episodes = 50

    # Calculate the number of episodes Marc watches per day
    episodes_per_day = total_episodes / 10

    # Calculate the number of days Marc needs to finish all the episodes
    days_to_finish = total_episodes / episodes_per_day

    result = days_to_finish
    return result

print(solution())