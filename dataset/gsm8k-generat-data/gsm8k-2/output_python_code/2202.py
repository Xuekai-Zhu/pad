def solution():
    """Ben has 20 eggs in the fridge. Yesterday, he ate 4 eggs in the morning and 3 in the afternoon. How many eggs does Ben have now?"""
    eggs_before = 20
    eggs_eaten = 4 + 3
    eggs_now = eggs_before - eggs_eaten
    result = eggs_now
    return result

print(solution())