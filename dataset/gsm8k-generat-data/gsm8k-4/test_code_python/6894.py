def solution():
    """Ben makes a sandwich that has 1250 calories total that has two strips of bacon with 125 calories each. What percentage of the sandwich's total calories come from bacon?"""
    # Define the total number of calories in the sandwich
    total_calories = 1250

    # Define the number of calories from each strip of bacon
    bacon_calories = 125

    # Calculate the total number of calories from the bacon
    total_bacon_calories = bacon_calories * 2

    # Calculate the percentage of calories from the bacon
    bacon_percentage = (total_bacon_calories / total_calories) * 100

    # Return the result
    result = bacon_percentage
    return result

print(solution())