def solution():
    goal = 3000  # Sandy's goal is to drink 3 liters, which is 3000 milliliters, of water in a day
    intake_per_round = 500  # Sandy drinks 500 milliliters of water every 2 hours
    rounds_needed = goal / intake_per_round  # Calculate the total rounds of drinking needed
    hours_needed = rounds_needed * 2  # Calculate the total hours needed
    result = hours_needed
    return result

print(solution())