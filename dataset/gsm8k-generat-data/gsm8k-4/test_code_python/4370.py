def solution():
    """Kaiden and Adriel were to pick a certain number of apples from their farm. After picking 400 apples each, they realized they still had to pick some more, so each picked 3/4 times as many as they had picked earlier. When they checked the pickup truck that was carrying the apples,
    they found out they still needed to pick 600 apples each to reach the target number. How many apples were they targeting to pick?"""
    
    # Calculate the total number of apples picked in the first round
    apples_first_round = 400 * 2

    # Calculate the number of apples picked in the second round
    apples_second_round = apples_first_round * 3/4

    # Calculate the total number of apples picked in both rounds
    total_apples_picked = apples_first_round + apples_second_round * 2

    # Calculate the target number of apples to be picked
    target_apples = total_apples_picked + 600 * 2
    
    result = target_apples
    return result

print(solution())