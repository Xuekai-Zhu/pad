def solution():
    """Jenny is planning her catering budget for her wedding. She's going to have 80 guests. 3 times as many guests want steak as chicken. If each steak entree costs $25 and each chicken entree costs $18, how much is the total catering budget?"""
    total_guests = 80
    steak_guests = 3 * total_guests / 4
    chicken_guests = total_guests / 4
    steak_cost = steak_guests * 25
    chicken_cost = chicken_guests * 18
    total_cost = steak_cost + chicken_cost
    result = total_cost
    return result

print(solution())