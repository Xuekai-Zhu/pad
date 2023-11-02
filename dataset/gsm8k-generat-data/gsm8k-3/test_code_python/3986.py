def solution():
    """48 children are trying to share a pack of sweets. After taking 4 sweets each, there is still a third of the original amount left. What is the original number of sweets in the pack?"""
    # Let x be the original number of sweets in the pack
    # After each child takes 4 sweets, there are still (2/3)x sweets left
    # So, (2/3)x sweets are shared by 48 children, each getting (2/3)x/48 sweets
    # Therefore, the total number of sweets in the pack is:
    # x = 48(4) + 48(2/3)x/48
    # Simplifying the above equation we will get the value of x as:
    x = 72
    result = x
    return result

print(solution())