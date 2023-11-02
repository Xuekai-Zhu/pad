def solution():
    """Bruce recently had a birthday. His aunt sent him a card with $75 and his grandfather sent him a card that had $150 in it. He wants to go on a trip to Europe soon, so he decides to put one-fifth of the money he got for his birthday in the bank. How much money did he put in the bank?"""
    # Define the money received from his aunt and grandfather
    aunt_money = 75
    grandfather_money = 150

    # Calculate the total amount of money received
    total_money = aunt_money + grandfather_money

    # Calculate one-fifth of the total money received
    bank_money = total_money / 5

    # Display the amount of money Bruce put in the bank
    result = bank_money
    return result

print(solution())