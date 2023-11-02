def solution():
    """Cecil has $600. Catherine has $250 less than twice as much as Cecil while Carmela has $50 more than twice Cecil's money. How much money do they have altogether?"""
    # Define Cecil's money
    cecil_money = 600

    # Define Catherine's money
    catherine_money = 2 * cecil_money - 250

    # Define Carmela's money
    carmela_money = 2 * cecil_money + 50

    # Calculate the total money they have altogether
    total_money = cecil_money + catherine_money + carmela_money

    # Display the total money
    result = total_money
    return result

print(solution())