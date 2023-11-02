def solution():
    # Calculate the time per shot and the shots per minute
    time_per_shot = 5  # Jason's weapon fires for 5 seconds per shot
    shots_per_minute = 60 / 15  # Jason fires his weapon every 15 seconds, so he fires 4 times per minute
    
    # Calculate the time Jason shoots flames per minute
    time_per_minute = time_per_shot * shots_per_minute
    
    result = time_per_minute
    return result

print(solution())