def solution():
    total_calories = 1250
    bacon_calories = 125 * 2

    # Calculate the percentage of calories that come from bacon
    percentage_from_bacon = bacon_calories / total_calories * 100
    result = percentage_from_bacon
    return result

print(solution())