def solution():
    time_in_minutes = 12
    lap_distance = 100
    laps_run = 24
    reward_per_meter = 3.5

    # Calculate the total distance run by the winner
    total_distance = lap_distance * laps_run

    # Calculate the total reward earned by the winner
    total_reward = total_distance / 100 * reward_per_meter

    # Calculate the average reward earned per minute
    reward_per_minute = total_reward / time_in_minutes
    result = reward_per_minute
    return result

print(solution())