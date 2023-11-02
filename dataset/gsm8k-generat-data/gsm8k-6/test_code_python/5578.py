def solution():
    # Calculate the total number of episodes in the TV series
    total_episodes = 3 * 20  # 3 seasons, each with 20 episodes

    # Calculate the number of days it will take Willy to finish the series
    days_to_finish = total_episodes // 2  # Willy watches 2 episodes a day

    result = days_to_finish
    return result

print(solution())