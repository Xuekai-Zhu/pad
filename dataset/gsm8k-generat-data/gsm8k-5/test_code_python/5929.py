def solution():
    bananas = 2
    apples = 2 * bananas  # There are twice as many apples as bananas
    total_fruits = 12

    # Calculate the number of oranges in the bowl
    oranges = total_fruits - bananas - apples

    result = oranges
    return result

print(solution())