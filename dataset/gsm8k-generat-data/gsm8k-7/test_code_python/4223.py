def solution():
    num_apples = 12
    apple_price = 2

    num_bananas = 4
    banana_price = 1

    num_oranges = 4
    orange_price = 3

    # Calculate the total cost of all apples
    total_apples_cost = num_apples * apple_price

    # Calculate the total cost of all bananas
    total_bananas_cost = num_bananas * banana_price

    # Calculate the total cost of all oranges
    total_oranges_cost = num_oranges * orange_price

    # Calculate the total cost of all fruit
    total_fruit_cost = total_apples_cost + total_bananas_cost + total_oranges_cost

    # Calculate the total number of pieces of fruit
    total_fruit_pieces = num_apples + num_bananas + num_oranges

    # Calculate the average cost per piece of fruit
    average_cost = total_fruit_cost / total_fruit_pieces
    result = average_cost
    return result

print(solution())