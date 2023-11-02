def solution():
    # Define the ratio of apples to oranges in the basket
    apple_to_orange_ratio = 4/1

    # Calculate the total number of fruits in the basket
    total_fruits = 15 / (1 + 4)

    # Calculate the number of apples Emiliano would have eaten
    apples_eaten = 2/3 * apple_to_orange_ratio * total_fruits

    # Calculate the number of oranges Emiliano would have eaten
    oranges_eaten = 2/3 * total_fruits

    # Calculate the total number of fruits Emiliano would have eaten
    total_fruits_eaten = apples_eaten + oranges_eaten
    result = total_fruits_eaten
    return result

print(solution())