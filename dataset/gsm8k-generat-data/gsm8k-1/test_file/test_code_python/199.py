def solution():
    """Carl’s favorite food is cheese. He ate a sandwich every day this week for lunch and used 2 slices of cheese on each sandwich. He ate cheese and egg omelets for breakfast 3 days in the week using one more slice per omelet than he did per sandwich. He made a big dish of macaroni and cheese to last him several dinners for the week and used 8 slices of cheese in it. How many slices of cheese did he use?"""
    slices_per_sandwich = 2
    sandwiches_per_week = 7
    slices_per_omelet = slices_per_sandwich + 1
    omelets_per_week = 3
    slices_in_mac_and_cheese = 8
    total_slices = (slices_per_sandwich * sandwiches_per_week) + (slices_per_omelet * omelets_per_week) + slices_in_mac_and_cheese
    result = total_slices
    return result

print(solution())