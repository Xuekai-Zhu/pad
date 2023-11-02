def solution():
    """When Jason plays the video game, Duty for Ashes, his mission to slay the dragon hoard requires that he fire his weapon on average every 15 seconds. And each time he fires his weapon, his power-fire setting allows him to shoot a flame for 5 seconds. On average, how many seconds per minute does Jason shoot flames at the dragon hoard?"""
    # Define the time between weapon firings and the length of time the flame is shot
    WEAPON_FIRING_TIME = 15
    FLAME_SHOOTING_TIME = 5

    # Calculate the number of weapon firings per minute
    weapon_firings_per_minute = 60 / WEAPON_FIRING_TIME

    # Calculate the length of time the flame is shot per minute
    flame_shooting_time_per_minute = weapon_firings_per_minute * FLAME_SHOOTING_TIME

    # Display the length of time the flame is shot per minute
    result = flame_shooting_time_per_minute
    return result

print(solution())