def solution():
    vampire_drain_rate = 3
    werewolf_eat_rate = 5
    total_people = 72

    # Calculate the combined rate of draining and eating
    combined_rate = vampire_drain_rate + werewolf_eat_rate

    # Calculate the number of weeks until they run out of people
    num_weeks = total_people / combined_rate
    result = num_weeks
    return result

print(solution())