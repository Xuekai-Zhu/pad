def solution():
    # Calculate the total eggs produced during Myrtle's absence
    total_eggs = 3 * 3 * 7

    # Subtract the eggs taken by the neighbor
    total_eggs -= 12

    # Subtract the eggs Myrtle dropped
    total_eggs -= 5

    result = total_eggs
    return result

print(solution())