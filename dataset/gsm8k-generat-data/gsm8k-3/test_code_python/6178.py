def solution():
    """Ibrahim wants to buy an MP3 player for 120 euros and a CD for 19 euros. He has 55 euros in savings. His father participates in his purchase by giving him 20 euros. How much money does Ibrahim lack?"""
    # Define the prices of the MP3 player and CD
    MP3_PRICE = 120
    CD_PRICE = 19

    # Define the amount of savings Ibrahim has and the amount his father contributes
    SAVINGS = 55
    FATHER_CONTRIBUTION = 20

    # Calculate the total cost of the MP3 player and CD
    total_cost = MP3_PRICE + CD_PRICE

    # Calculate the total amount of money Ibrahim has to spend
    total_budget = SAVINGS + FATHER_CONTRIBUTION

    # Calculate the amount of money Ibrahim lacks
    money_lack = total_cost - total_budget

    # Display the amount of money Ibrahim lacks
    result = money_lack
    return result

print(solution())