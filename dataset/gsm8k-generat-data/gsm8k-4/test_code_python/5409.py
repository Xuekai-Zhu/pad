def solution():
    """Bruce's aunt gave him $71 to spend on clothes at the mall. He bought 5 shirts that cost $5 each and a pair of pants that cost $26. How much money does Bruce have left to buy more clothes?"""
    # Define the total amount of money that Bruce has
    total_money = 71

    # Define the cost of the shirts
    shirt_cost = 5

    # Define the number of shirts purchased
    num_shirts = 5

    # Define the cost of the pants
    pant_cost = 26

    # Calculate the total cost of the clothes
    total_cost = (num_shirts * shirt_cost) + pant_cost

    # Calculate how much money Bruce has left
    money_left = total_money - total_cost

    # Display the amount of money Bruce has left
    result = money_left
    return result

print(solution())