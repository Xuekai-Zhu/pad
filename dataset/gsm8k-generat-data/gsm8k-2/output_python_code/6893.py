def solution():
    """Ben makes a sandwich that has 1250 calories total that has two strips of bacon with 125 calories each. What percentage of the sandwich's total calories come from bacon?"""
    sandwich_calories = 1250
    bacon_calories = 125 * 2
    bacon_percentage = (bacon_calories / sandwich_calories) * 100
    result = bacon_percentage
    return result

print(solution())