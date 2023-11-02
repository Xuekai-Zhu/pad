def solution():
    pears = 10
    oranges = 20
    apples = pears * 2
    fruit_given = 2
    total_fruit = pears + oranges + apples
    fruit_left = total_fruit - (fruit_given * 3)
    result = fruit_left
    
    return result

print(solution())