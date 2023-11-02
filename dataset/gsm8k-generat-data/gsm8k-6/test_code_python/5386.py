def solution():
    # Let x be the number of trolls hiding by the path
    x = 6

    # The number of trolls hiding under the bridge is 4 times the number by the path, minus 6
    under_bridge = 4*x - 6

    # The number of trolls hiding in the plains is half the number under the bridge
    in_plains = under_bridge / 2

    # The total number of trolls counted is the sum of all three groups
    total_trolls = x + under_bridge + in_plains

    result = total_trolls
    return result

print(solution())