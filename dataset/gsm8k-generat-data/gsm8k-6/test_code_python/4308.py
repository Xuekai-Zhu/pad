def solution():
    # Calculate the total number of rolls John bought
    total_cost = 15  # John spent 15 dollars
    cost_per_dozen = 5  # rolls cost 5 dollars per dozen
    rolls_per_dozen = 12  # there are 12 rolls in a dozen
    dozens_bought = total_cost // cost_per_dozen  # determine how many dozens John bought
    total_rolls = dozens_bought * rolls_per_dozen  # calculate the total number of rolls
    result = total_rolls
    return result

print(solution())