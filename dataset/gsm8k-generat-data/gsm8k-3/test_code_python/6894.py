def solution():
    """Ben makes a sandwich that has 1250 calories total that has two strips of bacon with 125 calories each. What percentage of the sandwich's total calories come from bacon?"""
    # Calculate the total calories from the bacon
    bacon_calories = 125 * 2

    # Calculate the percentage of calories from bacon
    percentage_bacon = (bacon_calories / 1250) * 100

    # Return the result rounded to 2 decimal places
    result = round(percentage_bacon, 2)
    return result

print(solution())