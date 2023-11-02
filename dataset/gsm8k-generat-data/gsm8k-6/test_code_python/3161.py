def solution():
    # Calculate the total number of eggs Trevor had
    total_eggs = 4 + 3 + 2 + 2  # Trevor got 4 eggs from Gertrude, 3 eggs from Blanche, 2 eggs from Nancy, and 2 eggs from Martha
    eggs_dropped = 2  # Trevor dropped 2 eggs while collecting them
    eggs_left = total_eggs - eggs_dropped  # Compute the number of eggs Trevor had left
    result = eggs_left
    return result

print(solution())