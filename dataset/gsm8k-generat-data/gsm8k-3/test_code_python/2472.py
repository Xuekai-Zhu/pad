def solution():
    """Karen packs peanut butter sandwiches in her daughter's lunch 2 randomly chosen days of the week. The other 3 school days, she packs a ham sandwich. She packs a piece of cake on one randomly chosen day and cookies the other four days. What is the probability, expressed as a percentage, that Karen packs a ham sandwich and cake on the same day?"""
    # Probability of packing a ham sandwich on any of the 3 school days
    p_ham = 3/5

    # Probability of packing a cake on any of the 5 school days
    p_cake = 1/5

    # Probability of packing a ham sandwich and cake on the same day
    p_both = p_ham * p_cake

    # Convert probability to percentage
    percentage = p_both * 100

    # Return the result as a string with 2 decimal places
    result = "{:.2f}%".format(percentage)
    return result

print(solution())