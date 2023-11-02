def solution():
    # Let x be the number of hops taken by the third frog
    x = 1
    # The second frog takes twice as many hops as the third
    y = 2*x
    # The first frog takes 4 times as many hops as the second
    z = 4*y
    # The total number of hops is 99
    total_hops = x + y + z
    # We want to find the number of hops taken by the second frog
    result = y
    return result

print(solution())