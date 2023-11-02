def solution():
    """Wendi brought home 4 chickens. After a few days, she brought home enough additional chickens to double the number 
    of chickens she owned. Then, a neighbor's dog ate one of her chickens. Finally, Wendi found an additional 4 less than 
    ten chickens and brought them home too. After this, how many chickens does Wendi have?"""
    
    # Starting with 4 chickens
    total_chickens = 4
    
    # After doubling the number of chickens
    total_chickens = total_chickens * 2
    
    # After the dog ate one of the chicken
    total_chickens = total_chickens - 1
    
    # After adding 4 less than ten chickens
    total_chickens = total_chickens + (10 - 4)
    
    result = total_chickens
    return result

print(solution())