def solution():
    
    pears = 10
    oranges = 20
    apples = 2 * pears
    total_fruits = pears + oranges + apples
    fruits_given_away = 2 * 3  
    fruits_left = total_fruits - fruits_given_away
    result = fruits_left
    return result

print(solution())