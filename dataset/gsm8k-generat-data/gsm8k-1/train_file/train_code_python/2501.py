def solution():
    """James gets bored with his game so decides to play a different one. That game promises 100 hours of gameplay but 80% of that is boring grinding. However, the expansion does add another 30 hours of enjoyable gameplay. How much enjoyable gameplay does James get?"""
    total_gameplay = 100
    boring_grinding = total_gameplay * 0.8
    enjoyable_gameplay = total_gameplay - boring_grinding + 30
    result = enjoyable_gameplay
    return result

print(solution())