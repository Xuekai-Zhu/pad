def solution():
    # Define the daily water goal and the size of Mary's glass
    daily_goal = 1.5 # liters
    glass_size = 0.25 # liters

    # Calculate the number of glasses Mary should drink to reach her goal
    num_glasses = daily_goal / glass_size
    result = int(num_glasses) # round down to a whole number of glasses
    return result

print(solution())