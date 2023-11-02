def solution():
    """Jenny is planning her catering budget for her wedding. She's going to have 80 guests. 3 times as many guests want steak as chicken. If each steak entree costs $25 and each chicken entree costs $18, how much is the total catering budget?"""
    num_guests = 80
    steak_ratio = 3
    chicken_ratio = 1

    num_steak = (num_guests / (steak_ratio + chicken_ratio)) * steak_ratio
    num_chicken = (num_guests / (steak_ratio + chicken_ratio)) * chicken_ratio

    cost_steak = num_steak * 25
    cost_chicken = num_chicken * 18

    total_cost = cost_steak + cost_chicken

    result = total_cost
    return result

print(solution())