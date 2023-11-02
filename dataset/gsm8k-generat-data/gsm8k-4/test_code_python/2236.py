def solution():
    """Evie is collecting seashells while at the beach. Each day she collects her favorite 10 shells. At the end of 6 days, she gives 2 shells to her brother. How many shells does she have left?"""
    # Define the initial number of shells
    initial_shells = 0

    # Calculate the total number of shells collected after 6 days
    total_shells = 6 * 10

    # Calculate the number of shells left after giving 2 to her brother
    shells_left = total_shells - 2

    result = shells_left
    return result

print(solution())