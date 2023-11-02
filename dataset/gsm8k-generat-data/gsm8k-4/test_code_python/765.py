def solution():
    """Brenda picks 250 peaches. When she sorts through them, only 60% are fresh, and Brenda has to throw 15 away for being too small. How many peaches does Brenda have left?"""
    # Define the initial number of peaches and the percentage of fresh peaches
    initial_peaches = 250
    fresh_percentage = 0.6

    # Calculate the number of fresh peaches
    fresh_peaches = initial_peaches * fresh_percentage

    # Subtract the number of peaches that Brenda had to throw away
    remaining_peaches = fresh_peaches - 15

    # return the result
    result = remaining_peaches
    return result

print(solution())