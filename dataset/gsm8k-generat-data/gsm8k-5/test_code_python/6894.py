def solution():
    bacon_calories = 125 * 2  # Two strips of bacon with 125 calories each
    sandwich_calories = 1250  # The sandwich has a total of 1250 calories

    # Calculate the percentage of calories that come from bacon
    bacon_percentage = (bacon_calories / sandwich_calories) * 100
    result = bacon_percentage
    return result

print(solution())