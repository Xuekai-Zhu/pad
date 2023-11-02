def solution():
    """Ben wants to pick 56 sugar snap peas. At his current rate of picking, all will be picked in seven minutes. How long, in minutes, would it take Ben to pick 72 sugar snap peas?"""
    # Define the current number of peas Ben can pick per minute
    PICK_RATE = 56/7

    # Calculate the time it would take Ben to pick 72 peas
    time = 72 / PICK_RATE

    # Display the time in minutes
    result = time
    return result

print(solution())