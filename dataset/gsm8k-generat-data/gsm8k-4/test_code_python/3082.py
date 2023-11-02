def solution():
    """Mimi picked up 2 dozen seashells on the beach.  Kyle found twice as many shells as Mimi and put them in his pocket. Leigh grabbed one-third of the shells that Kyle found.  How many seashells did Leigh have?"""
    # Define the number of seashells picked up by Mimi
    mimi_shells = 2 * 12

    # Calculate the number of seashells picked up by Kyle
    kyle_shells = mimi_shells * 2

    # Calculate the number of seashells picked up by Leigh
    leigh_shells = kyle_shells / 3

    # return the result
    result = leigh_shells
    return result

print(solution())