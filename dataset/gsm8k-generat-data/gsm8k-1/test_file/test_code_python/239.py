def solution():
    """Jason has a phone plan of 1000 minutes per month. Every day he has a 15-minute call with his boss, and he's had 300 extra minutes of call this month to other people. How many minutes does Jason have left if this month has 30 days?"""
    plan_minutes = 1000
    boss_call_minutes = 15 * 30
    extra_minutes = 300
    total_minutes = boss_call_minutes + extra_minutes
    minutes_left = plan_minutes - total_minutes
    result = minutes_left
    return result

print(solution())