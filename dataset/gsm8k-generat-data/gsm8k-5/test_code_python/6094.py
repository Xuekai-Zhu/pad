def solution():
    time_seals = x  # We don't know how long Walter spent looking at the seals
    time_penguins = 8 * time_seals  # Walter spent eight times as long looking at the penguins as he did looking at the seals
    time_elephants = 13  # Walter spent 13 minutes looking at the elephants
    total_time = 130  # Walter spent 2 hours and 10 minutes (which is 130 minutes) at the zoo

    # Write an equation that relates the total time to the time spent looking at all three animals
    # (the time spent looking at the seals, penguins, and elephants)
    # and solve for the time spent looking at the seals
    time_seals = (total_time - time_penguins - time_elephants) / 9
    result = time_seals
    return result

print(solution())