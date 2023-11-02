def solution():
    num_small_apples = 6
    small_apple_price = 1.5

    num_medium_apples = 6
    medium_apple_price = 2

    num_big_apples = 8
    big_apple_price = 3

    # Calculate the total cost of all small apples
    total_small_apple_cost = num_small_apples * small_apple_price

    # Calculate the total cost of all medium apples
    total_medium_apple_cost = num_medium_apples * medium_apple_price

    # Calculate the total cost of all big apples
    total_big_apple_cost = num_big_apples * big_apple_price

    # Calculate the total cost of all apples
    total_cost = total_small_apple_cost + total_medium_apple_cost + total_big_apple_cost
    result = total_cost
    return result

print(solution())