def solution():
    """James gets bored with his game so decides to play a different one. That game promises 100 hours of gameplay but 80% of that is boring grinding. However, the expansion does add another 30 hours of enjoyable gameplay. How much enjoyable gameplay does James get?"""
    total_playtime = 100
    grinding_time = total_playtime * 0.8
    expansion_time = 30
    enjoyable_time = total_playtime - grinding_time + expansion_time
    result = enjoyable_time
    return result

print(solution())