def solution():
    # Calculate the total number of gems Tom purchased
    total_gems = 100 * 250  # the game gives 100 gems for each dollar you spend
    bonus_gems = 0.2 * total_gems  # 20% bonus of more gems
    total_gems += bonus_gems

    result = total_gems
    return result

print(solution())