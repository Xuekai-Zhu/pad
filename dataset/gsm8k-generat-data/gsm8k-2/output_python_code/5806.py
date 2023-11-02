def solution():
    """It takes Emmalyn and her research team, the Polar Bears, 30 minutes to fully navigate around a volcanic island. On Saturday, they decided to start off by rounding the island once. They then re-grouped and planned out the rest of their weekend research schedule. They completed 10 more round that day and then went home. When they came on Sunday, they were able to complete 15 rounds. Calculate the total time, in minutes, the Polar Bears spent circling the island over that weekend."""
    time_to_round_once = 30
    rounds_on_saturday = 11
    rounds_on_sunday = 15
    total_time = ((rounds_on_saturday + rounds_on_sunday) * time_to_round_once) + time_to_round_once
    result = total_time
    return result

print(solution())