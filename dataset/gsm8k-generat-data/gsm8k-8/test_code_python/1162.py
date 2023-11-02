def solution():
    granola_bars_made = 200
    granola_bars_eaten_by_parents = 80
    granola_bars_left = granola_bars_made - granola_bars_eaten_by_parents
    granola_bars_per_child = 20

    # Calculate the number of children by dividing the remaining granola bars with the granola bars per child
    num_children = granola_bars_left / granola_bars_per_child
    result = num_children
    return result

print(solution())