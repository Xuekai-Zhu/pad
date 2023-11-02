def solution():
    """Ben makes a sandwich that has 1250 calories total that has two strips of bacon with 125 calories each. What percentage of the sandwich's total calories come from bacon?"""
    total_calories = 1250
    bacon_calories = 125 * 2
    percent_bacon_calories = (bacon_calories / total_calories) * 100
    result = percent_bacon_calories
    return result

print(solution())