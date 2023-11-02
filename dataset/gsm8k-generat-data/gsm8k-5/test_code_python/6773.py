def solution():
    current_earnings = 20 + 60 + 15 + 40  # Jerry's current total earnings
    nights_worked = 4  # Jerry has worked 4 nights so far
    target_average_earnings = 50  # Jerry wants to make an average of $50 in tips per night
    nights_left_to_work = 1  # Jerry has one more night left to work

    # Calculate the amount Jerry needs to make on the final night to earn an average of $50 per night
    required_earnings = (target_average_earnings * (nights_worked + nights_left_to_work)) - current_earnings
    result = required_earnings
    return result

print(solution())