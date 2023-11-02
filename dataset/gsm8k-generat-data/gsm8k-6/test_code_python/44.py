def solution():
    # Calculate the amount of money James spends on each expense
    food = 0.3 * 1000  # 30% of budget spent on food
    accommodation = 0.15 * 1000  # 15% of budget spent on accommodation
    entertainment = 0.25 * 1000  # 25% of budget spent on entertainment
    coursework = 1000 - (food + accommodation + entertainment)  # remaining budget spent on coursework materials
    result = coursework
    return result

print(solution())