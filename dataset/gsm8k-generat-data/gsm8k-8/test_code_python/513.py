def solution():
    # Calculate the number of apples
    pears = 10
    apples = 2 * pears
    oranges = 20

    # Subtract 2 from each fruit given to sister
    pears -= 2
    apples -= 2
    oranges -= 2
    
    # Calculate the total number of fruits remaining
    total_fruits = pears + apples + oranges
    result = total_fruits
    return result

print(solution())