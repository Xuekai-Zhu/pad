def solution():
    # Define the number of team members and days
    num_team_members = 15
    num_days = 3

    # Calculate the number of blankets collected on the first day
    blankets_day1 = num_team_members * 2

    # Calculate the number of blankets collected on the second day
    blankets_day2 = blankets_day1 * 3

    # Calculate the total number of blankets collected
    total_blankets = blankets_day1 + blankets_day2 + 22

    result = total_blankets
    return result

print(solution())