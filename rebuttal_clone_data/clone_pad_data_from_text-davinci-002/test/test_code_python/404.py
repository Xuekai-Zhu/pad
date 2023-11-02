def solution():
    total_oranges = 180
    ratio = 2
    emily_oranges = total_oranges / (ratio + 1)
    alice_oranges = total_oranges - emily_oranges
    result = alice_oranges
    return result

print(solution())