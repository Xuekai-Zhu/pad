def solution():
    """Tom spends $250 to buy gems in a game he plays. The game gives 100 gems for each dollar you spend. Since he bought so many gems he got a 20% bonus of more gems. How many gems did he end up with?"""
    # Define the cost per gem
    cost_per_gem = 1 / 100
    
    # Define the initial cost and the cost after the bonus
    initial_cost = 250
    bonus_cost = initial_cost * 1.2
    
    # Calculate the total number of gems purchased
    total_gems = bonus_cost / cost_per_gem
    
    result = round(total_gems)
    return result

print(solution())