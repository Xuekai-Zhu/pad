def solution():
    """It takes Emmalyn and her research team, the Polar Bears, 30 minutes to fully navigate around a volcanic island. On Saturday, they decided to start off by rounding the island once. They then re-grouped and planned out the rest of their weekend research schedule. They completed 10 more round that day and then went home. When they came on Sunday, they were able to complete 15 rounds. Calculate the total time, in minutes, the Polar Bears spent circling the island over that weekend."""
    time_per_round = 30
    rounds_on_saturday = 11
    rounds_on_sunday = 15
    total_rounds = rounds_on_saturday + rounds_on_sunday
    total_time = total_rounds * time_per_round
    result = total_time
    return result

print(solution())