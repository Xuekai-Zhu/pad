def solution():
    # Calculate the number of guests who want steak and chicken
    steak_guests = 3 * chicken_guests     # 3 times as many guests want steak as chicken
    total_guests = 80
    chicken_guests = total_guests / 4     # assume 1/4 guests want chicken

    # Calculate the total cost of steak and chicken entrees
    steak_cost = steak_guests * 25       # each steak costs $25
    chicken_cost = chicken_guests * 18   # each chicken costs $18
    total_cost = steak_cost + chicken_cost     # total catering budget

    result = total_cost
    return result

print(solution())