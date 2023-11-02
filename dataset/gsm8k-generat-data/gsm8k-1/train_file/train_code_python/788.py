def solution():
    """James hurt himself exercising. The pain subsided after 3 days, but he knew that the injury would take at least 5 times that long to fully heal. After that, he wanted to wait another 3 days before he started working out again. If he wants to wait 3 weeks after that to start lifting heavy again, how long until he can lift heavy again?"""
    healing_time = 3*5 # 5 times the length of initial pain
    recovery_time = healing_time + 3 # waiting 3 additional days after healing
    waiting_time = recovery_time + 21 # waiting 3 weeks after recovery
    result = waiting_time
    return result

print(solution())