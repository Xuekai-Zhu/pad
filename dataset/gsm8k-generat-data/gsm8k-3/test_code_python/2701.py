def solution():
    """A crate can hold 20 kilograms of tomatoes. Tommy has 3 crates which he bought for $330. He wants to sell the tomatoes for $6 per 1 kilogram but 3 kilograms of tomatoes were rotten. How much will be Tommy's profit from selling those tomatoes?"""
    # Define the amount of tomatoes that can fit in one crate
    TOMATOES_PER_CRATE = 20

    # Define the cost of the three crates
    CRATE_COST = 330

    # Calculate the total amount of tomatoes Tommy has
    total_tomatoes = TOMATOES_PER_CRATE * 3

    # Calculate the weight of the rotten tomatoes
    rotten_tomatoes = 3

    # Calculate the weight of the good tomatoes
    good_tomatoes = total_tomatoes - rotten_tomatoes

    # Calculate the total income from selling the good tomatoes
    total_income = good_tomatoes * 6

    # Calculate Tommy's profit
    profit = total_income - CRATE_COST

    # Display Tommy's profit
    result = profit
    return result

print(solution())