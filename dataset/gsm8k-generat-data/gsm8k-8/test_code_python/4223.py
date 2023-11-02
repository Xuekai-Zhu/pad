def solution():
    # Define the cost of each type of fruit
    apple_cost = 2
    banana_cost = 1
    orange_cost = 3

    # Define the number of fruits Marcia buys
    num_apples = 12
    num_bananas = 4
    num_oranges = 4

    # Calculate the total cost of all the fruit
    total_cost = num_apples * apple_cost + num_bananas * banana_cost + num_oranges * orange_cost

    # Calculate the average cost per piece of fruit
    num_fruit = num_apples + num_bananas + num_oranges
    average_cost = total_cost / num_fruit
    result = average_cost
    return result

print(solution())