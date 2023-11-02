def solution():
    # Find the number of seashells Leo collected
    leo_collected = 59 - 11 - 24  # Henry and Paul collected 11 and 24 seashells respectively
    # Calculate how many seashells Leo has left after giving a quarter of his collection
    leo_left = leo_collected - (leo_collected / 4)
    # Calculate the total number of seashells they have now
    total_shells = 11 + 24 + leo_left
    result = total_shells
    return result

print(solution())