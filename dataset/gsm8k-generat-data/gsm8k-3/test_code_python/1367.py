def solution():
    """An entrepreneur is crowdfunding a new business effort. He has three different dollar amount levels of financial backing options
    and each level is ten times as high as the previous one. He needs to raise $12000 to get his business off the ground. He succeeded 
    after getting two backers at the highest level of financial backing, three at the second level, and ten at the lowest level. 
    How many dollars was the highest level of financial backing?"""
    
    # Define the number of backers at each level and the total amount raised
    level3_backers = 10
    level2_backers = 3
    level1_backers = 2
    total_raised = 12000
    
    # Determine the ratio between the levels
    level3_ratio = 1
    level2_ratio = 10 * level3_ratio
    level1_ratio = 10 * level2_ratio
    
    # Calculate the total amount raised at each level
    level3_total = level3_backers * level3_ratio
    level2_total = level2_backers * level2_ratio
    level1_total = level1_backers * level1_ratio
    
    # Calculate the highest level of financial backing
    highest_level = level3_total
    
    # Display the highest level of financial backing
    result = highest_level
    return result

print(solution())