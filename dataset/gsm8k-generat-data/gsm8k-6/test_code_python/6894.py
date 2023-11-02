def solution():
    bacon_calories = 2 * 125  # calories from two strips of bacon
    sandwich_calories = 1250  # total calories in the sandwich
    bacon_percent = bacon_calories / sandwich_calories * 100  # percent of calories from bacon
    result = bacon_percent
    return result

print(solution())