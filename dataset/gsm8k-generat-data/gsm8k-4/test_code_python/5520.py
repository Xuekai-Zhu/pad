def solution():
    """John's new computer cost $1500. He needs to get a monitor and other peripherals that cost 1/5 that much. He also wants to upgrade the $300 video card in the base computer with one that costs twice as much. How much did he spend?"""
    # Define the cost of the base computer, peripherals and video card
    computer_cost = 1500
    peripherals_cost = computer_cost / 5
    video_card_cost = 300 * 2

    # Calculate the total cost
    total_cost = computer_cost + peripherals_cost + video_card_cost

    # Return the result
    result = total_cost
    return result

print(solution())