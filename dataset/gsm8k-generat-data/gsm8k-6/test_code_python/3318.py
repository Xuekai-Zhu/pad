def solution():
    # Calculate the total number of fruits Kannon will have tonight
    apples = 3 + 4  # Kannon will have 4 more apples than last night
    bananas = 10 * 1  # Kannon will have 10 times as many bananas as she ate last night (1 banana)
    oranges = 2 * apples  # Kannon will have twice as many oranges as apples she'll have today
    total_fruits = apples + bananas + oranges
    
    # Calculate the total number of fruits Kannon had last night
    last_night_fruits = 3 + 1 + 4  # 3 apples, 1 banana, and 4 oranges
    
    # Calculate the total number of fruits Kannon has eaten so far in the two meals
    fruits_eaten = last_night_fruits + total_fruits
    result = fruits_eaten
    return result

print(solution())