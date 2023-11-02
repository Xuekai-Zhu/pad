def solution():
    candy_bars_per_week = 2  # Kim's dad buys her 2 candy bars every week
    eaten_per_cycle = 1  # Kim eats 1 candy bar every 4 weeks
    cycles = 16  # Kim saved candy bars for 16 weeks

    # Calculate the total number of candy bars saved during the 16 weeks
    saved_bars = (candy_bars_per_week - eaten_per_cycle) * cycles

    result = saved_bars
    return result

print(solution())