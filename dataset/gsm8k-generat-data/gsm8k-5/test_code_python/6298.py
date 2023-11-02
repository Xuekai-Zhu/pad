def solution():
    total_episodes = 50  # Marc bought 50 episodes of "Friends"
    daily_progress = 1/10  # Marc watches 1/10 of the episodes per day

    # Calculate the number of days Marc needs to finish all 50 episodes
    days_needed = total_episodes / daily_progress
    result = days_needed
    return result

print(solution())