def solution():
    """Johnny has been playing guitar for a while now. He practices the same amount each day. As of 20 days ago he had half as much practice as he has currently. How many days will pass before Johnny has 3 times as much practice as he does currently?"""
    current_practice = 0
    days_passed = 0
    while current_practice < 3 * current_practice:
        days_passed += 1
        current_practice += 1
        if days_passed > 20:
            current_practice *= 2
    result = days_passed
    return result

print(solution())