def solution():
    """When Jason plays the video game, Duty for Ashes, his mission to slay the dragon hoard requires that he fire his weapon on average every 15 seconds. And each time he fires his weapon, his power-fire setting allows him to shoot a flame for 5 seconds. On average, how many seconds per minute does Jason shoot flames at the dragon hoard?"""
    shots_per_minute = 60 / 15
    seconds_shooting_per_shot = 5
    seconds_shooting_per_minute = shots_per_minute * seconds_shooting_per_shot
    result = seconds_shooting_per_minute
    return result

print(solution())