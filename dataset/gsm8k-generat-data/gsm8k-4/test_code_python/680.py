def solution():
    """Cecil has $600. Catherine has $250 less than twice as much as Cecil while Carmela has $50 more than twice Cecil's money. How much money do they have altogether?"""
    # Define the amount of money Cecil has
    cecil_money = 600

    # Calculate the amount of money Catherine has
    catherine_money = (2 * cecil_money) - 250

    #Calculate the amount of money Carmela has
    carmela_money = (2 * cecil_money) + 50

    # Calculate the total amount of money they have altogether
    total_money = cecil_money + catherine_money + carmela_money

    result = total_money
    return result

print(solution())