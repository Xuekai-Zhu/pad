def solution():
    """John's new computer cost $1500. He needs to get a monitor and other peripherals that cost 1/5 that much. He also wants to upgrade the $300 video card in the base computer with one that costs twice as much. How much did he spend?"""
    # Define the cost of the computer and peripherals
    COMPUTER_COST = 1500
    PERIPHERALS_COST = COMPUTER_COST * (1 / 5)

    # Define the cost of the upgraded video card
    UPGRADED_VIDEOCARD_COST = 300 * 2

    # Calculate the total cost
    total_cost = COMPUTER_COST + PERIPHERALS_COST + UPGRADED_VIDEOCARD_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())