def solution():
    # Calculate the number of eggs in the nests in the first tree
    eggs_in_first_tree = 2 * 5

    # Calculate the total number of eggs in both nests in the first tree and the nest in the other tree
    total_eggs = eggs_in_first_tree + 3

    # Add the eggs in the nest in the front yard to the total
    total_eggs += 4

    result = total_eggs
    return result

print(solution())