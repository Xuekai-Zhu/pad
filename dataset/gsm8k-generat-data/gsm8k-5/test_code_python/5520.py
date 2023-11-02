def solution():
    base_cost = 1500  # The cost of the base computer
    monitor_cost = base_cost // 5  # The cost of the monitor and other peripherals
    upgraded_card_cost = 2 * 300  # The cost of the upgraded video card

    # Calculate the total cost of the system
    total_cost = base_cost + monitor_cost + upgraded_card_cost
    result = total_cost
    return result

print(solution())