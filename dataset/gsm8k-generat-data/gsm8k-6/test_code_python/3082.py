def solution():
    # Calculate the total number of seashells picked up by Mimi
    mimi_shells = 2 * 12  # 2 dozen seashells

    # Calculate the number of seashells found by Kyle
    kyle_shells = 2 * mimi_shells  # twice as many shells as Mimi

    # Calculate the number of seashells grabbed by Leigh
    leigh_shells = kyle_shells / 3  # one-third of the shells that Kyle found

    result = leigh_shells
    return result

print(solution())