def solution():
    """There were 100 jelly beans in a bag to be given away on Halloween. Out of the 40 children taking part in the Halloween celebration, 80% were allowed to draw jelly beans from the bag. Each child drew two jelly beans out of the bag. How many jelly beans remained in the bag after the children took their share?"""
    total_jelly_beans = 100
    participating_children = int(40 * 0.8)
    jelly_beans_drawn = participating_children * 2
    remaining_jelly_beans = total_jelly_beans - jelly_beans_drawn
    result = remaining_jelly_beans
    return result

print(solution())