def solution():
    """John's new computer cost $1500. He needs to get a monitor and other peripherals that cost 1/5 that much. He also wants to upgrade the $300 video card in the base computer with one that costs twice as much. How much did he spend?"""
    computer_cost = 1500
    peripheral_cost = computer_cost / 5
    monitor_cost = peripheral_cost - 100  # assuming $100 for other peripherals
    video_card_upgrade_cost = 2 * 300
    total_cost = computer_cost + peripheral_cost + monitor_cost + video_card_upgrade_cost
    result = total_cost
    return result

print(solution())