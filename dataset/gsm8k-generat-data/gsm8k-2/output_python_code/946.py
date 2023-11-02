def solution():
    """Johnny has been playing guitar for a while now. He practices the same amount each day. As of 20 days ago he had half as much practice as he has currently. How many days will pass before Johnny has 3 times as much practice as he does currently?"""
    days_since_20_days_ago = 20
    current_practice = days_since_20_days_ago * 2
    days_until_3x_practice = 0
    while current_practice * 3 > days_since_20_days_ago + days_until_3x_practice:
        days_until_3x_practice += 1

    result = days_until_3x_practice
    return result

print(solution())