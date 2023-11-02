def solution():
    """Mike decides to do more pull-ups to increase his strength for climbing. He uses the greasing the groove technique where every time he goes into a certain room he does 2 pull-ups. He decides to use his office. He goes in there 5 times a day every day. How many pull-ups does he do a week?"""
    # Define the number of times Mike goes to his office in a day
    times_per_day = 5

    # Calculate the number of pull-ups Mike does in a day
    pullups_per_day = 2 * times_per_day

    # Calculate the number of pull-ups Mike does in a week
    pullups_per_week = pullups_per_day * 7

    # Return the result
    result = pullups_per_week
    return result

print(solution())