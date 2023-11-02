def solution():
    # Calculate the number of seashells in the jar in a month (4 weeks)
    seashells_this_week = 50
    increment = 20
    total_seashells = seashells_this_week
    for i in range(1, 4):
        seashells_this_week += increment
        total_seashells += seashells_this_week
    result = total_seashells
    return result

print(solution())