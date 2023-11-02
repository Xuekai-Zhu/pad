def solution():
    
    total_oranges = 180
    alice_oranges = 0
    while alice_oranges < total_oranges:
        alice_oranges += 2
        total_oranges -= 1
    result = alice_oranges
    return result

print(solution())