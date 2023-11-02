def solution():
    num_team_members = 15

    # Calculate the number of blankets collected on the first day
    blankets_day1 = num_team_members * 2

    # Calculate the number of blankets collected on the second day
    blankets_day2 = blankets_day1 * 3

    # Calculate the number of blankets collected on the last day
    blankets_day3 = 22

    # Calculate the total number of blankets collected in the three days
    total_blankets = blankets_day1 + blankets_day2 + blankets_day3
    result = total_blankets
    return result

print(solution())