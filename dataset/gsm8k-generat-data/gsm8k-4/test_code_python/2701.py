def solution():
    """A crate can hold 20 kilograms of tomatoes. Tommy has 3 crates which he bought for $330. He wants to sell the tomatoes for $6 per 1 kilogram but 3 kilograms of tomatoes were rotten. How much will be Tommy's profit from selling those tomatoes?"""
    # Define the capacity of a crate and the number of crates
    CRATE_CAPACITY = 20
    NUM_CRATES = 3

    # Define the weight of the rotten tomatoes
    ROTTEN_WEIGHT = 3

    # Calculate the total weight of usable tomatoes
    total_weight = CRATE_CAPACITY * NUM_CRATES - ROTTEN_WEIGHT

    # Calculate the total amount earned from selling the usable tomatoes
    total_earned = total_weight * 6

    # Calculate the total cost of purchasing the crates
    total_cost = 330

    # Calculate the profit
    profit = total_earned - total_cost

    # return the result
    result = profit
    return result

print(solution())