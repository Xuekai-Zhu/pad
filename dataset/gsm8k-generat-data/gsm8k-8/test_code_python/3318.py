def solution():
    # Calculate the number of fruits she had last night
    fruits_last_night = 3 + 1 + 4
    # Calculate the number of fruits she plans to have today
    apples_today = 4 + 3
    bananas_today = 10 * 1
    oranges_today = 2 * 4
    fruits_today = apples_today + bananas_today + oranges_today
    # Calculate the total number of fruits she will eat in both meals
    total_fruits = fruits_last_night + fruits_today
    result = total_fruits
    return result

print(solution())