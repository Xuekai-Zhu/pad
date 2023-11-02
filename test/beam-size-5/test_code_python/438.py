def solution():
    initial_temp = 40  # Marcus's house is 40 degrees initially
    baking_time = 3  # Marcus spends 3 hours baking
    oven_temp = initial_temp - (baking_time * 5)  # Marcus raises the house's temperature by 5 degrees every hour the oven is on it raises the house's temperature by 5 degrees
    window_open_time = 30  # Marcus opens a window for 30 minutes
    cool_down_time = 2  # The house cools down 2 degrees for every 10 minutes the window is open

    # Calculate the house's final temperature
    final_temp = initial_temp + (baking_time * oven_temp) + (window_open_time * cool_down_time)
    result = final_temp
    return result

print(solution())