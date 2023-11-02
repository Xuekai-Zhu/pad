def solution():
    """Carly is making burgers for a neighborhood BBQ. Each burger needs to be cooked for 4 minutes on each side. Carly can fit 5 burgers on the grill at once. If half her 30 guests want 2 burgers and the other half each want 1, how long will it take Carly to cook all the burgers?"""
    # Calculate the total number of burgers needed
    total_burgers = 30 * 1.5

    # Calculate the number of batches of 5 burgers needed
    batches = total_burgers // 5
    remaining_burgers = total_burgers % 5

    # Calculate the total cooking time
    total_time = (batches * 2 + (remaining_burgers > 0)) * 4

    # Return the result
    result = total_time
    return result

print(solution())