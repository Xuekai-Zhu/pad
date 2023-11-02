def solution():
    """Fabian bought a brand new computer mouse and keyboard to be able to work from home. The cost of the keyboard was three times greater than the cost of the mouse. If the mouse cost $16, how much did Fabian spent on his new accessories?"""
    # Define the cost of the mouse and the ratio of keyboard cost to mouse cost
    mouse_cost = 16
    keyboard_to_mouse_ratio = 3

    # Calculate the cost of the keyboard
    keyboard_cost = mouse_cost * keyboard_to_mouse_ratio

    # Calculate the total cost of the accessories
    total_cost = mouse_cost + keyboard_cost

    # Return the result
    result = total_cost
    return result

print(solution())