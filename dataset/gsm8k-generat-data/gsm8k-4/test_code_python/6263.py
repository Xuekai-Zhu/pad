def solution():
    """Freddie and his team are collecting blankets for three days to be donated to the Children Shelter Organization. There are 15 people on the team. On the first day, each of them gave 2 blankets. On the second day, they tripled the number they collected on the first day by asking door-to-door. On the last day, they set up boxes at schools and got a total of 22 blankets. How many blankets did they collect for the three days for donation?"""
    # Define the number of people on the team
    num_people = 15

    # Calculate the number of blankets collected on the first day
    blankets_first_day = num_people * 2

    # Calculate the number of blankets collected on the second day
    blankets_second_day = blankets_first_day * 3

    # Calculate the number of blankets collected on the third day
    blankets_third_day = 22

    # Calculate the total number of blankets collected
    total_blankets = blankets_first_day + blankets_second_day + blankets_third_day

    # Return the result
    result = total_blankets
    return result

print(solution())