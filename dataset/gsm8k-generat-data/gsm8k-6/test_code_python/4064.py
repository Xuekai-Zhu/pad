def solution():
    # Calculate the cost of one chocolate bar
    cost_of_magazine = 1 
    cost_of_four_chocolates = 2 * cost_of_magazine  # cost of four chocolate bars is equal to the cost of 8 magazines
    cost_of_one_chocolate = cost_of_four_chocolates / 4  

    # Calculate the cost of a dozen chocolate bars
    cost_of_dozen_chocolates = 12 * cost_of_one_chocolate  
    result = cost_of_dozen_chocolates
    return result

print(solution())