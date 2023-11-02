def solution():
    """Tim host a show and they film multiple episodes per day. Each episode is 20 minutes long and it takes 50% longer than that to film each episode. Each week they show 5 episodes. How many hours would it take to film 4 weeks of episodes?"""
    # Define the length of a single episode in minutes
    episode_length = 20

    # Calculate the length of time it takes to film a single episode, including 50% extra time
    filming_time = episode_length * 1.5

    # Calculate the total time to film a week's worth of episodes
    weekly_filming_time = 5 * filming_time

    # Calculate the total time to film 4 weeks worth of episodes
    total_filming_time = 4 * weekly_filming_time

    # Convert the total filming time from minutes to hours
    total_filming_hours = total_filming_time / 60

    # return the result
    result = total_filming_hours
    return result

print(solution())