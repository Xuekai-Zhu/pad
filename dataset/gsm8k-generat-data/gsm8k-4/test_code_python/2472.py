def solution():
    """Karen packs peanut butter sandwiches in her daughter's lunch 2 randomly chosen days of the week. The other 3 school days, she packs a ham sandwich. She packs a piece of cake on one randomly chosen day and cookies the other four days. What is the probability, expressed as a percentage, that Karen packs a ham sandwich and cake on the same day?"""
    # Define the probability of choosing a ham sandwich and cake on the same day
    ham_prob = 3/5
    cake_prob = 1/5
    prob = ham_prob * cake_prob

    # Convert probability to percentage
    result = prob * 100
    return result

print(solution())