def solution():
    """Alice and Emily are selling oranges at the farmer's market. Alice sold twice as many oranges as Emily did. In total, they sold 180 oranges. How many oranges did Alice sell?"""
    # Let x be the number of oranges Emily sold
    # Then Alice sold 2x oranges
    x = 180 / 3
    alice_oranges = 2 * x

    # Display the number of oranges Alice sold
    result = alice_oranges
    return result

print(solution())