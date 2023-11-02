I'm sorry, but a solution cannot be provided for the question about Samantha's last name as it is incomplete and lacks necessary information. 

def solution():
    """When Marcus wakes up, his house is 40 degrees. He spends 3 hours baking, and every hour the oven is on it raises the house's temperature by 5 degrees. Then Marcus opens a window for 30 minutes, and the house cools down 2 degrees for every 10 minutes the window is open. What is the house's final temperature?"""
    initial_temp = 40
    bake_time = 3
    oven_temp_increase = 5
    open_window_time = 30
    window_cooling_rate = 2
    window_cooling_time = open_window_time / 10
    total_oven_temp_increase = bake_time * oven_temp_increase
    total_window_cooling = window_cooling_time * window_cooling_rate
    final_temp = initial_temp + total_oven_temp_increase - total_window_cooling
    result = final_temp
    return result

print(solution())