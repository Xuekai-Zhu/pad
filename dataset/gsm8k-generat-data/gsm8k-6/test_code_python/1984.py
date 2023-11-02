def solution():
    # Calculate the total calories Jacob ate for the day
    total_calories = 400 + 900 + 1100

    # Calculate the calories over Jacob's daily limit
    over_limit = total_calories - 1800

    result = over_limit
    return result

print(solution())