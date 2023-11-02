def solution():
    # Calculate the time it takes for Maryann to pick the lock on all three pairs of handcuffs
    time_to_pick_cheap_handcuffs = 6  # time to pick lock on cheap handcuffs
    time_to_pick_expensive_handcuffs = 8  # time to pick lock on expensive handcuffs
    time_to_pick_all_handcuffs = 3*time_to_pick_expensive_handcuffs + 3*time_to_pick_cheap_handcuffs
    
    result = time_to_pick_all_handcuffs
    return result

print(solution())