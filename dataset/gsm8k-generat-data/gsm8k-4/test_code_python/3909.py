def solution():
    """John is performing in 3 plays. Each play has 5 Acts. He wears 2 wigs per act. Each wig cost $5. He drops one of the plays and sells all of the wigs for that play for $4. How much money did he spend?"""
    # Define the number of plays and acts
    plays = 3
    acts_per_play = 5

    # Define the number of wigs worn per act
    wigs_per_act = 2

    # Define the cost per wig
    wig_cost = 5

    # Calculate the total number of wigs worn
    total_wigs = plays * acts_per_play * wigs_per_act

    # Calculate the total cost of all the wigs
    total_cost = total_wigs * wig_cost

    # Calculate the number of wigs from one play
    wigs_from_one_play = acts_per_play * wigs_per_act

    # Calculate the total profit from selling the wigs from one play
    total_profit = wigs_from_one_play * 4

    # Subtract the profit from the total cost to get the final amount spent
    final_amount = total_cost - total_profit

    # return the result
    result = final_amount
    return result

print(solution())