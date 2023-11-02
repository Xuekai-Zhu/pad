def solution():
    """Jenny is planning her catering budget for her wedding. She's going to have 80 guests. 3 times as many guests want steak as chicken. If each steak entree costs $25 and each chicken entree costs $18, how much is the total catering budget?"""
    # Define the number of guests and the ratio of steak to chicken
    total_guests = 80
    steak_to_chicken_ratio = 3

    # Calculate the number of guests who want chicken and steak
    chicken_guests = total_guests / (steak_to_chicken_ratio + 1)
    steak_guests = steak_to_chicken_ratio * chicken_guests

    # Calculate the cost of the chicken entrees and the steak entrees
    chicken_cost = chicken_guests * 18
    steak_cost = steak_guests * 25

    # Calculate the total catering budget
    total_cost = chicken_cost + steak_cost

    # return the result
    result = total_cost
    return result

print(solution())