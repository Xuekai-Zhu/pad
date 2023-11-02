def solution():
    # Probability of packing a ham sandwich on a given day
    p_ham = 3/5

    # Probability of packing cake on a given day
    p_cake = 1/5

    # Probability of packing a ham sandwich AND cake on the same day
    p_both = p_ham * p_cake

    # Convert probability to percentage
    percentage = p_both * 100
    result = percentage
    return result

print(solution())