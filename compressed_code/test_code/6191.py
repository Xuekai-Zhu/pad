def solution():
    
    jelly_beans_in_bag = 100
    children_participating = 40
    percentage_allowed = 80
    jelly_beans_drawn_per_child = 2
    total_jelly_beans_drawn = (children_participating * percentage_allowed / 100) * jelly_beans_drawn_per_child
    jelly_beans_remaining = jelly_beans_in_bag - total_jelly_beans_drawn
    result = jelly_beans_remaining
    
    return result

print(solution())