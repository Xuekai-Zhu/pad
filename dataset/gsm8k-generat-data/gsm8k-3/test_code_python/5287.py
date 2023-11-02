def solution():
    """Dennis lives two floors above Charlie. Charlie lives on a floor whose number is 1/4 Frank's floor number. Frank lives on the 16th floor. What floor does Dennis live on?"""
    # Define Frank's floor number
    frank_floor = 16

    # Calculate Charlie's floor number
    charlie_floor = frank_floor * 0.25

    # Calculate Dennis's floor number
    dennis_floor = charlie_floor + 2

    # Display Dennis's floor number
    result = dennis_floor
    return result

print(solution())