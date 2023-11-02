def solution():
    """When Jason plays the video game, Duty for Ashes, his mission to slay the dragon hoard requires that he fire his weapon on average every 15 seconds. And each time he fires his weapon, his power-fire setting allows him to shoot a flame for 5 seconds. On average, how many seconds per minute does Jason shoot flames at the dragon hoard?"""
    # Define the time between weapon fires and the flame duration
    time_between_fires = 15
    flame_duration = 5

    # Calculate the number of flames per minute
    flames_per_minute = 60 / time_between_fires

    # Calculate the total time spent shooting flames per minute
    total_flame_time = flames_per_minute * flame_duration

    # Return the result
    result = total_flame_time
    return result

print(solution())