def solution():
    team_size = 15  # Freddie's team has 15 people
    blankets_first_day = 2 * team_size  # Each member gave 2 blankets on the first day
    blankets_second_day = 3 * blankets_first_day  # They tripled the number of blankets collected on the first day
    blankets_third_day = 22  # They collected 22 blankets on the last day

    # Calculate the total number of blankets collected
    total_blankets = blankets_first_day + blankets_second_day + blankets_third_day
    result = total_blankets
    return result

print(solution())