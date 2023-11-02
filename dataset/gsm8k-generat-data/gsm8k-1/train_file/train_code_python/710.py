def solution():
    """Alice and Emily are selling oranges at the farmer's market. Alice sold twice as many oranges as Emily did. In total, they sold 180 oranges. How many oranges did Alice sell?"""
    total_oranges = 180
    alice_oranges = 0.0
    emily_oranges = 0.0
    for i in range(total_oranges+1):
        if i*2 + i == total_oranges:
            alice_oranges = i*2
            emily_oranges = i
            break
    result = alice_oranges
    return result

print(solution())