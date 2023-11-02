def solution():
    """Andy is a lawyer who's working on two lawsuits. The first lawsuit has a 30% chance of paying out $5,000,000 upon a win and $0 if he loses it. The second lawsuit has a 50% chance of paying out $1,000,000 if Andy loses and a 50% chance of paying out $2,000,000 if he wins. Expressed as a percentage, how much more likely is it that Andy loses both lawsuits compared to winning both of them?"""
    # Probability of losing both lawsuits is the product of the probabilities of losing each lawsuit
    probability_of_losing_both = 0.7 * 0.5  # 0.35 or 35%
    
    # Probability of winning both lawsuits is the product of the probabilities of winning each lawsuit
    probability_of_winning_both = 0.3 * 0.5  # 0.15 or 15%
    
    # Calculate the difference between the two probabilities as a percentage
    difference = abs(probability_of_losing_both - probability_of_winning_both) * 100
    
    result = difference
    return result

print(solution())