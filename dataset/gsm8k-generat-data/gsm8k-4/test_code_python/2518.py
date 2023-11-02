def solution():
    """Elsa gets 500 MB of cell phone data each month. If she spends 300 MB watching Youtube and 2/5 of what's left on Facebook, how many MB of data does she have left?"""
    # Define the initial amount of data
    data = 500

    # Deduct the amount of data used to watch Youtube
    data -= 300

    # Deduct 2/5 of the remaining data for Facebook
    data -= (2/5) * (500 - 300)

    result = data
    return result

print(solution())