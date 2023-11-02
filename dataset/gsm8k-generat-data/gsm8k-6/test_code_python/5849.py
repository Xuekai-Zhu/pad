def solution():
    # Calculate the total number of episodes watched by Max during the week
    total_episodes = 4  # the show airs only on weekdays
    total_hours = total_episodes * 0.5  # each episode airs for 30 min or 0.5 hours
    # Subtract the Friday episode as Max missed it
    total_hours -= 0.5
    result = total_hours
    return result

print(solution())