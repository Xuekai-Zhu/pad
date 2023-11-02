def solution():
    """Ben has 20 eggs in the fridge. Yesterday, he ate 4 eggs in the morning and 3 in the afternoon. How many eggs does Ben have now?"""
    # Define the initial number of eggs
    eggs = 20

    # Calculate the number of eggs eaten yesterday
    eaten_yesterday = 4 + 3

    # Subtract the eaten eggs from the initial number
    eggs_now = eggs - eaten_yesterday

    # return the result
    result = eggs_now
    return result

print(solution())