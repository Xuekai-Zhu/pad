def solution():
    # Let's assume x is the original number of geese in the formation
    x = 2 * 12  # Since only half stayed in the formation, after the split there were 2 groups of 12 geese each

    # After the split, there were x/2 geese in each group
    # 4 geese flew up and joined the original x/2 geese to form the new V formation
    # So, the total number of geese in the new V formation is (x/2) + 4

    # Therefore, we can write the equation (x/2) + 4 = 12
    # Solving for x, we get x = 16

    result = 16
    return result

print(solution())