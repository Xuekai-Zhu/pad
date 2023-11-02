def solution():
    """Freddie and his team are collecting blankets for three days to be donated to the Children Shelter Organization. There are 15 people on the team. On the first day, each of them gave 2 blankets. On the second day, they tripled the number they collected on the first day by asking door-to-door. On the last day, they set up boxes at schools and got a total of 22 blankets. How many blankets did they collect for the three days for donation?"""
    # Define the number of people on the team
    TEAM_SIZE = 15

    # Calculate the number of blankets collected on the first day
    blankets_day1 = 2 * TEAM_SIZE

    # Calculate the number of blankets collected on the second day
    blankets_day2 = 3 * blankets_day1

    # Calculate the number of blankets collected on the third day
    blankets_day3 = 22 - blankets_day1 - blankets_day2

    # Calculate the total number of blankets collected
    total_blankets = blankets_day1 + blankets_day2 + blankets_day3

    # Display the total number of blankets collected
    result = total_blankets
    return result

print(solution())