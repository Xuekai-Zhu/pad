def solution():
    """Freddie and his team are collecting blankets for three days to be donated to the Children Shelter Organization. There are 15 people on the team. On the first day, each of them gave 2 blankets. On the second day, they tripled the number they collected on the first day by asking door-to-door. On the last day, they set up boxes at schools and got a total of 22 blankets. How many blankets did they collect for the three days for donation?"""

    team_size = 15
    blankets_first_day = 2 * team_size
    blankets_second_day = 3 * blankets_first_day
    blankets_third_day = 22
    total_blankets = blankets_first_day + blankets_second_day + blankets_third_day

    return total_blankets

print(solution())