def solution():
    """Bruce's aunt gave him $71 to spend on clothes at the mall. He bought 5 shirts that cost $5 each and a pair of pants that cost $26. How much money does Bruce have left to buy more clothes?"""
    # Define the amount Bruce has to spend and the cost of each item
    BUDGET = 71
    SHIRT_PRICE = 5
    PANTS_PRICE = 26

    # Calculate the total cost of the shirts and pants
    shirt_cost = 5 * SHIRT_PRICE
    pants_cost = PANTS_PRICE

    # Calculate the total cost of all the clothes
    total_cost = shirt_cost + pants_cost

    # Calculate how much money Bruce has left to spend
    money_left = BUDGET - total_cost

    # Display how much money Bruce has left to spend
    result = money_left
    return result

print(solution())