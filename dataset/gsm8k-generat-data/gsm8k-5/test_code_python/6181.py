def solution():
    num_supplements = 5  # Antonia has 5 different supplements
    total_pills = 0

    # Determine how many pills are in each bottle
    for i in range(num_supplements):
        if i < 3:
            pills_per_bottle = 120
        else:
            pills_per_bottle = 30

        # Calculate the total number of pills in all bottles
        total_pills += pills_per_bottle

    # Calculate how many pills Antonia uses each day
    pills_per_day = num_supplements

    # Calculate how many pills Antonia uses in 2 weeks
    pills_used = pills_per_day * 14

    # Calculate how many pills Antonia has left in all bottles
    pills_left = total_pills - pills_used
    result = pills_left
    return result

print(solution())