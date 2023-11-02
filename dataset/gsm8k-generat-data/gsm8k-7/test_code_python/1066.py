def solution():
    george_oranges = 45
    amelia_apples = george_oranges + 5
    george_apples = 15
    amelia_oranges = george_oranges - 18

    # Calculate the total number of oranges
    total_oranges = george_oranges + amelia_oranges

    # Calculate the total number of apples
    total_apples = george_apples + amelia_apples

    # Calculate the total number of fruits
    total_fruits = total_oranges + total_apples
    result = total_fruits
    return result

print(solution())