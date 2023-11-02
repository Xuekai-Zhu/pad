def solution():
    """Freddie and his team are collecting blankets for three days to be donated to the Children Shelter Organization. There are 15 people on the team. On the first day, each of them gave 2 blankets. On the second day, they tripled the number they collected on the first day by asking door-to-door. On the last day, they set up boxes at schools and got a total of 22 blankets. How many blankets did they collect for the three days for donation?"""
    team_size = 15
    first_day_collection = team_size * 2
    second_day_collection = first_day_collection * 3
    third_day_collection = 22
    total_collection = first_day_collection + second_day_collection + third_day_collection
    result = total_collection
    return result

print(solution())