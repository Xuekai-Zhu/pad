def solution():
    """When Jason plays the video game, Duty for Ashes, his mission to slay the dragon hoard requires that he fire his weapon on average every 15 seconds.
    And each time he fires his weapon, his power-fire setting allows him to shoot a flame for 5 seconds. On average, how many seconds per minute does Jason shoot flames at the dragon hoard?"""
    fire_rate = 15
    flame_duration = 5
    shots_per_minute = 60 / fire_rate
    seconds_of_flame_per_shot = flame_duration
    seconds_of_flame_per_minute = shots_per_minute * seconds_of_flame_per_shot
    result = seconds_of_flame_per_minute
    return result

print(solution())