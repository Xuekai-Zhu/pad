def solution():
    # Define the number of oranges and apples picked by George
    george_oranges = 45
    george_apples = george_oranges + 5

    # Define the number of oranges and apples picked by Amelia
    amelia_oranges = george_oranges - 18
    amelia_apples = george_apples - 15

    # Calculate the total number of fruits picked
    total_fruits = george_oranges + george_apples + amelia_oranges + amelia_apples
    result = total_fruits
    return result

print(solution())