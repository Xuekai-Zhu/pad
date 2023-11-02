def solution():
    # Calculate Mimi's number of seashells
    mimi_shells = 2 * 12

    # Calculate Kyle's number of seashells and convert to an integer
    kyle_shells = int(2 * mimi_shells)

    # Calculate Leigh's number of seashells and round to the nearest whole number
    leigh_shells = round(kyle_shells / 3)

    result = leigh_shells
    return result

print(solution())