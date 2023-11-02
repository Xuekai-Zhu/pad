def solution():
    """Mimi picked up 2 dozen seashells on the beach.  Kyle found twice as many shells as Mimi and put them in his pocket. Leigh grabbed one-third of the shells that Kyle found.  How many seashells did Leigh have?"""
    # Define the number of shells Mimi found
    mimi_shells = 2 * 12

    # Define the number of shells Kyle found
    kyle_shells = 2 * mimi_shells

    # Define the number of shells Leigh found
    leigh_shells = kyle_shells / 3

    # Display the number of shells Leigh found
    result = leigh_shells
    return result

print(solution())