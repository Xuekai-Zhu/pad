def solution():
    """Chad has 100 apples and each apple has different sizes and different price ranges. Each small apple cost $1.5, medium apple cost $2, and big apples cost $3. If Donny bought 6 small and medium apples and also 8 big apples, how much will Donny have to pay for all of it?"""
    # Define the prices of small, medium, and big apples
    SMALL_PRICE = 1.5
    MEDIUM_PRICE = 2
    BIG_PRICE = 3

    # Define the number of small, medium, and big apples that Donny bought
    small_apples = 6
    medium_apples = 6  # assuming 6 small and 6 medium apples were bought
    big_apples = 8

    # Calculate the total cost of all the apples
    total_cost = (small_apples * SMALL_PRICE) + (medium_apples * MEDIUM_PRICE) + (big_apples * BIG_PRICE)

    result = total_cost
    return result

print(solution())