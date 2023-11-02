def solution():
    num_supplements = 5

    num_long_bottles = 3
    long_bottle_size = 120

    num_short_bottles = 2
    short_bottle_size = 30

    num_days = 14
    num_pills_per_day = num_supplements

    # Calculate the total number of pills Antonia needs for 2 weeks
    total_pills_needed = num_days * num_pills_per_day

    # Calculate the total number of pills from the long bottles
    total_long_bottle_pills = num_long_bottles * long_bottle_size

    # Calculate the total number of pills from the short bottles
    total_short_bottle_pills = num_short_bottles * short_bottle_size

    # Calculate the total number of pills Antonia has left
    total_pills_left = total_long_bottle_pills + total_short_bottle_pills - total_pills_needed
    result = total_pills_left
    return result

print(solution())