def solution():
    """James hurt himself exercising. The pain subsided after 3 days, but he knew that the injury would take at least 5 times that long to fully heal. After that, he wanted to wait another 3 days before he started working out again. If he wants to wait 3 weeks after that to start lifting heavy again, how long until he can lift heavy again?"""
    pain_duration = 3
    full_healing_duration = 5 * pain_duration
    rest_duration = 3
    waiting_duration = 3 * 7  # 3 weeks in days

    total_duration = pain_duration + full_healing_duration + rest_duration + waiting_duration
    result = total_duration
    return result

print(solution())