def solution():
    # Probability of packing a ham sandwich on a given day
    prob_ham = 3/5  

    # Probability of packing cake on a given day
    prob_cake = 1/5  

    # Probability of packing both ham sandwich and cake on the same day
    prob_both = prob_ham * prob_cake  

    # Convert probability to percentage
    percentage_prob = prob_both * 100  
    result = percentage_prob
    return result

print(solution())