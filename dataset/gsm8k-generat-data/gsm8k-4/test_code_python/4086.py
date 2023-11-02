def solution():
    """The number of dishes Sandrine washed was 10 more than the number of bananas Charles cooked. Also, the number of bananas Charles cooked was 3 times the number of pears he picked. If Charles picked 50 pears, how many dishes did Sandrine wash?"""
    # Define the number of pears Charles picked
    pears_picked = 50
    
    # Calculate the number of bananas cooked by Charles
    bananas_cooked = pears_picked * 3
    
    # Calculate the number of dishes washed by Sandrine
    dishes_washed = bananas_cooked + 10
    
    # return the result
    result = dishes_washed
    return result

print(solution())