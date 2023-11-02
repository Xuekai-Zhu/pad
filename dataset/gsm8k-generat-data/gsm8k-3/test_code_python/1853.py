def solution():
    """How many shirts should Shenny pack for her next vacation if she's planning to use the same shirt when departing on Monday and returning on Sunday and two different shirts each other day?"""
    # Shenny will need 2 shirts for each day except Monday and Sunday
    shirts_needed = 2 * 5 # 5 days from Tuesday to Saturday

    # Shenny will wear the same shirt on Monday and Sunday
    shirts_needed += 1

    # Display the total number of shirts needed
    result = shirts_needed
    return result

print(solution())