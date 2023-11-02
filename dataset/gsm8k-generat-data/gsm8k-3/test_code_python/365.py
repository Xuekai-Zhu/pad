def solution():
    """Tony paid $7 for 2 dozen apples and 1 bunch of bananas. Arnold paid $5 for 1 dozen apples and 1 bunch of bananas. How much does a bunch of bananas cost?"""
    # Define the cost of a dozen apples for Tony and Arnold
    TONY_APPLE_PRICE = 7 / 2 / 12
    ARNOLD_APPLE_PRICE = 5 / 1 / 12

    # Define the number of apples each person bought
    tony_apples = 2 * 12
    arnold_apples = 1 * 12

    # Calculate the cost of the apples for each person
    tony_apple_cost = tony_apples * TONY_APPLE_PRICE
    arnold_apple_cost = arnold_apples * ARNOLD_APPLE_PRICE

    # Calculate the total cost of the bananas for each person
    tony_banana_cost = 7 - tony_apple_cost
    arnold_banana_cost = 5 - arnold_apple_cost

    # Calculate the cost of a bunch of bananas
    bunch_cost = (tony_banana_cost + arnold_banana_cost) / 2

    # Display the cost of a bunch of bananas
    result = bunch_cost
    return result

print(solution())