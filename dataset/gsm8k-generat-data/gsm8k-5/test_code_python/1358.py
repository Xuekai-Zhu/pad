def solution():
    num_guests_steak = 3 * (80 / 4)  # Three times as many guests want steak as chicken, assuming each table seats 4 guests
    num_guests_chicken = 80 - num_guests_steak
    cost_steak = num_guests_steak * 25
    cost_chicken = num_guests_chicken * 18
    total_cost = cost_steak + cost_chicken
    result = total_cost
    return result

print(solution())