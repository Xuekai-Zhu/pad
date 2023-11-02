def solution():
    """Chad has 100 apples and each apple has different sizes and different price ranges. Each small apple cost $1.5, medium apple cost $2, and big apples cost $3. If Donny bought 6 small and medium apples and also 8 big apples, how much will Donny have to pay for all of it?"""
    # Define the cost for each size of apple
    SMALL_COST = 1.5
    MEDIUM_COST = 2
    BIG_COST = 3

    # Define the number of each size of apple Donny bought
    small_apples = 6
    medium_apples = 6
    big_apples = 8

    # Calculate the total cost for each size of apple
    small_cost = small_apples * SMALL_COST
    medium_cost = medium_apples * MEDIUM_COST
    big_cost = big_apples * BIG_COST

    # Calculate the total cost for all the apples
    total_cost = small_cost + medium_cost + big_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())