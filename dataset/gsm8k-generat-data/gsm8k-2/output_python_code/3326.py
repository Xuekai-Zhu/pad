def solution():
    """Tom spends $250 to buy gems in a game he plays. The game gives 100 gems for each dollar you spend. Since he bought so many gems he got a 20% bonus of more gems. How many gems did he end up with?"""
    dollars_spent = 250
    gems_per_dollar = 100
    total_gems = dollars_spent * gems_per_dollar
    bonus_percentage = 0.2
    bonus_gems = total_gems * bonus_percentage
    total_gems += bonus_gems
    result = total_gems
    return result

print(solution())