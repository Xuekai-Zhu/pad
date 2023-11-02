def solution():
    
    last_night_apples = 3
    last_night_bananas = 1
    last_night_oranges = 4
    today_apples = last_night_apples + 4
    today_bananas = last_night_bananas * 10
    today_oranges = today_apples * 2
    total_fruits = last_night_apples + last_night_bananas + last_night_oranges + today_apples + today_bananas + today_oranges
    result = total_fruits
    return result

print(solution())