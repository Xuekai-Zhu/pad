def solution():
    # Calculate the total number of blankets collected by Freddie's team
    blankets_collected_day1 = 2 * 15  # each team member gave 2 blankets on the first day
    blankets_collected_day2 = 3 * blankets_collected_day1  # they tripled the number collected on the first day
    blankets_collected_day3 = 22  # they got 22 blankets from setting up boxes at schools
    total_blankets_collected = blankets_collected_day1 + blankets_collected_day2 + blankets_collected_day3
    result = total_blankets_collected
    return result

print(solution())