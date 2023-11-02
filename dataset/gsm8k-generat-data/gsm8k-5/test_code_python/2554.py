def solution():
    small_apple_price = 1.5  # Each small apple costs $1.5
    medium_apple_price = 2  # Each medium apple costs $2
    big_apple_price = 3  # Each big apple costs $3
    num_small_apples = 6  # Donny bought 6 small apples
    num_medium_apples = 6  # Donny also bought 6 medium apples
    num_big_apples = 8  # Donny bought 8 big apples

    # Calculate the total cost of Donny's purchase
    total_cost = (small_apple_price * num_small_apples) + (medium_apple_price * num_medium_apples) + (
                big_apple_price * num_big_apples)
    result = total_cost
    return result

print(solution())