def solution():
    """Troy is thinking of buying a new computer that is worth $80. He has initially saved $50 and plans to sell his old computer for $20. How much more money does he need so he could buy the new computer?"""
    # Define the cost of the new computer, Troy's savings, and the amount he plans to sell his old computer for
    COMPUTER_COST = 80
    SAVINGS = 50
    OLD_COMPUTER_SALE = 20

    # Calculate the total amount of money Troy has
    total_money = SAVINGS + OLD_COMPUTER_SALE

    # Calculate how much more money Troy needs to buy the new computer
    additional_money = COMPUTER_COST - total_money

    # Display how much more money Troy needs
    result = additional_money
    return result

print(solution())