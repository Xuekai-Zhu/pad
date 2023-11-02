def solution():
    """Alice and Emily are selling oranges at the farmer's market. Alice sold twice as many oranges as Emily did. In total, they sold 180 oranges. How many oranges did Alice sell?"""
    total_oranges = 180
    alice_oranges = 0
    while alice_oranges < total_oranges:
        alice_oranges += 2
        total_oranges -= 1
    result = alice_oranges
    return result

print(solution())