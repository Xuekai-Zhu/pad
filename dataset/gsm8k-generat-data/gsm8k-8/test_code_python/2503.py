def solution():
    # Calculate Alden's current number of nephews
    aldens_nephews_now = 2 * 50

    # Calculate Vihaan's current number of nephews
    vihaans_nephews_now = aldens_nephews_now + 60

    # Calculate the total number of nephews
    total_nephews = aldens_nephews_now + vihaans_nephews_now

    result = total_nephews
    return result

print(solution())