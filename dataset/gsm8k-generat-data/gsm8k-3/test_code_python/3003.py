def solution():
    """In mid-May, the depth of a river in Moreland is measured. By mid-June, the river is 10 feet deeper than mid-May. By mid-July, the river is three times deeper than mid-June. If the river is 45 feet deep in mid-July, how many feet deep was the river in mid-May?"""
    # Let x be the depth of the river in mid-May
    # Then the depth of the river in mid-June is x + 10
    # And the depth of the river in mid-July is 3(x + 10)
    # We are given that the depth of the river in mid-July is 45
    # So we can solve for x as follows:
    # 3(x + 10) = 45
    # 3x + 30 = 45
    # 3x = 15
    # x = 5

    # Therefore, the river was 5 feet deep in mid-May
    result = 5
    return result

print(solution())