def solution():
    """There were 100 jelly beans in a bag to be given away on Halloween. Out of the 40 children taking part in the Halloween celebration, 80% were allowed to draw jelly beans from the bag. Each child drew two jelly beans out of the bag. How many jelly beans remained in the bag after the children took their share?"""
    jelly_beans_in_bag = 100
    children_participating = 40
    percentage_allowed = 80
    jelly_beans_drawn_per_child = 2
    total_jelly_beans_drawn = (children_participating * percentage_allowed / 100) * jelly_beans_drawn_per_child
    jelly_beans_remaining = jelly_beans_in_bag - total_jelly_beans_drawn
    result = jelly_beans_remaining
    
    return result

print(solution())