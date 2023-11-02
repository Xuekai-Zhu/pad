def solution():
    mashed_scoops = 23  # Gomer ate 5 less than 23 scoops of mashed potatoes
    less_than_6 = 6 - 3  # It takes 3 less than 6 potatoes to make 1 less than 3 scoops
    mashed_scoops_eaten = mashed_scoops - 5  # Gomer ate 5 less than 23 scoops of mashed potatoes

    # Calculate the number of potatoes Gomer ate
    potatoes_eaten = (3 * mashed_scoops_eaten) - less_than_6
    result = potatoes_eaten
    return result

print(solution())