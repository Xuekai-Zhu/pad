def solution():
    """Tom spends $250 to buy gems in a game he plays.  The game gives 100 gems for each dollar you spend.  Since he bought so many gems he got a 20% bonus of more gems. How many gems did he end up with?"""
    # Define the number of gems per dollar spent
    GEMS_PER_DOLLAR = 100

    # Calculate the total number of gems Tom received without the bonus
    total_gems = 250 * GEMS_PER_DOLLAR

    # Calculate the number of bonus gems Tom received
    bonus_gems = 0.2 * total_gems

    # Calculate the total number of gems Tom ended up with
    total_gems += bonus_gems

    # Display the total number of gems Tom ended up with
    result = total_gems
    return result

print(solution())