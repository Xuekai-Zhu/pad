def solution():
    """Kaiden and Adriel were to pick a certain number of apples from their farm. After picking 400 apples each, they realized they still had to pick some more, so each picked 3/4 times as many as they had picked earlier. When they checked the pickup truck that was carrying the apples, they found out they still needed to pick 600 apples each to reach the target number. How many apples were they targeting to pick?"""
    initial_pick = 400
    second_pick = 3/4 * initial_pick
    remaining_pick = 600
    total_pick_needed = initial_pick + second_pick + remaining_pick
    target_pick = total_pick_needed * 2
    result = target_pick
    return result

print(solution())