def solution():
    """Mrs. Thompson bought 3 chickens for $3 each. She also bought a bag of potatoes. Mrs. Thompson paid $15 in total. How much did the potatoes cost?"""
    # Define the price of each chicken
    CHICKEN_PRICE = 3

    # Define the number of chickens purchased
    chickens = 3

    # Calculate the total cost of the chickens
    chicken_cost = CHICKEN_PRICE * chickens

    # Calculate the cost of the potatoes
    potato_cost = 15 - chicken_cost

    # Display the cost of the potatoes
    result = potato_cost
    return result

print(solution())