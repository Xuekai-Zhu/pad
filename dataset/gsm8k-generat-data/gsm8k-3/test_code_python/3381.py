def solution():
    """Five shirts are bought. Of the 5 shirts, there are 3 shirts that cost $15 each. The remaining shirts are $20 each. What is the cost, in dollars, of all 5 shirts?"""
    # Define the cost of each type of shirt
    CHEAP_SHIRT_PRICE = 15
    EXPENSIVE_SHIRT_PRICE = 20

    # Define the number of each type of shirt purchased
    cheap_shirts = 3
    expensive_shirts = 2

    # Calculate the total cost of the cheap shirts
    cheap_cost = CHEAP_SHIRT_PRICE * cheap_shirts

    # Calculate the total cost of the expensive shirts
    expensive_cost = EXPENSIVE_SHIRT_PRICE * expensive_shirts

    # Calculate the total cost of all the shirts
    total_cost = cheap_cost + expensive_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())