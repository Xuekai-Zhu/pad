def solution():
    # Calculate the total number of fruits Gabby picked in the summer
    watermelon = 1
    peaches = watermelon + 12
    plums = 3 * watermelon
    total_fruits = watermelon + peaches + 2*plums  # Gabby planted a watermelon vine, a peach tree, and two plum trees
    result = total_fruits
    return result

print(solution())