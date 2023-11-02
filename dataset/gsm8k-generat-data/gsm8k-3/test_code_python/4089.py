def solution():
    """Martine has 6 more than twice as many peaches as Benjy. Benjy has one-third as many peaches as Gabrielle. If Martine has 16 peaches, how many does Gabrielle have?"""
    
    # Define the number of peaches Martine has
    martine_peaches = 16
    
    # Calculate the number of peaches Benjy has
    benjy_peaches = (martine_peaches - 6) // 2
    
    # Calculate the number of peaches Gabrielle has
    gabrielle_peaches = benjy_peaches * 3
    
    # Display the number of peaches Gabrielle has
    result = gabrielle_peaches
    return result

print(solution())