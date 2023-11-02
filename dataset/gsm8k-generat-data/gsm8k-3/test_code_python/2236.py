def solution():
    """Evie is collecting seashells while at the beach.  Each day she collects her favorite 10 shells.  At the end of 6 days, she gives 2 shells to her brother.  How many shells does she have left?"""
    # Define the number of shells collected per day
    SHELLS_PER_DAY = 10

    # Define the number of days Evie collected shells
    days_collected = 6

    # Calculate the total number of shells collected
    total_shells = SHELLS_PER_DAY * days_collected

    # Subtract the number of shells given to Evie's brother
    shells_left = total_shells - 2

    # Display the number of shells Evie has left
    result = shells_left
    return result

print(solution())