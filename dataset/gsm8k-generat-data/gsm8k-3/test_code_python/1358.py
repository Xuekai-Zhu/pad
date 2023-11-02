def solution():
    """Jenny is planning her catering budget for her wedding. She's going to have 80 guests. 3 times as many guests want steak as chicken. If each steak entree costs $25 and each chicken entree costs $18, how much is the total catering budget?"""
    # Define the number of guests and the ratio of steak to chicken
    NUM_GUESTS = 80
    STEAK_CHICKEN_RATIO = 3

    # Calculate the number of guests who want steak and chicken
    num_steak = STEAK_CHICKEN_RATIO * (NUM_GUESTS / (1 + STEAK_CHICKEN_RATIO))
    num_chicken = NUM_GUESTS - num_steak

    # Calculate the cost of the steak and chicken entrees
    steak_cost = num_steak * 25
    chicken_cost = num_chicken * 18

    # Calculate the total catering budget
    total_cost = steak_cost + chicken_cost

    # Display the total catering budget
    result = total_cost
    return result

print(solution())