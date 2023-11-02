def solution():
    """John is performing in 3 plays. Each play has 5 Acts. He wears 2 wigs per act. Each wig costs $5. He drops one of the plays and sells all of the wigs for that play for $4. How much money did he spend?"""
    # Define the number of plays and acts
    plays = 3
    acts_per_play = 5

    # Define the cost of one wig
    WIG_COST = 5

    # Calculate the total number of acts
    total_acts = plays * acts_per_play

    # Calculate the total number of wigs used
    total_wigs = total_acts * 2

    # Calculate the total cost of all the wigs
    total_cost = total_wigs * WIG_COST

    # Subtract the cost of the wigs from the one play that was dropped and add the money from selling the wigs
    total_cost -= 10 * 2  # 10 wigs from the dropped play, each wig sold for $4
    total_cost += 20  # 10 wigs from the dropped play sold for $4 each

    # Display the total cost
    result = total_cost
    return result

print(solution())