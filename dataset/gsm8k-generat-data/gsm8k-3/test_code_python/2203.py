def solution():
    """Ben has 20 eggs in the fridge. Yesterday, he ate 4 eggs in the morning and 3 in the afternoon. How many eggs does Ben have now?"""
    # Define the initial number of eggs
    initial_eggs = 20

    # Calculate the number of eggs Ben ate yesterday
    eggs_yesterday = 4 + 3

    # Calculate the number of eggs Ben has now
    remaining_eggs = initial_eggs - eggs_yesterday

    # Display the number of eggs Ben has now
    result = remaining_eggs
    return result

print(solution())