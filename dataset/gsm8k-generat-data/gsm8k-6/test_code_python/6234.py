def solution():
    # Let's say the third frog takes x number of hops
    # The second frog takes twice as many as the third, so it takes 2x hops
    # The first frog takes 4 times as many as the second, so it takes 8x hops
    # The total number of hops is 99, so we can write an equation: x + 2x + 8x = 99
    # Solving for x, we get x = 9
    # Therefore, the second frog took 2x = 18 hops to cross the road
    result = 18
    return result

print(solution())