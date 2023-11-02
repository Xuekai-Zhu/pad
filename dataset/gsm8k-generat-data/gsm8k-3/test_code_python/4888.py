def solution():
    """Patrick has been saving money to buy a bicycle that costs $150. He saved half the price but he then lent $50 to his friend. How much money does Patrick have now?"""
    # Define the cost of the bicycle
    BICYCLE_PRICE = 150

    # Calculate how much Patrick saved
    saved_money = BICYCLE_PRICE / 2

    # Calculate how much money Patrick has now after lending $50 to his friend
    money_now = saved_money - 50

    # Display how much money Patrick has now
    result = money_now
    return result

print(solution())