def solution():
    jelly_beans_in_bag = 100  # There were 100 jelly beans in the bag
    participating_children = 40  # There were 40 children taking part in the celebration
    allowed_children = int(participating_children * 0.8)  # 80% of children were allowed to draw jelly beans
    jelly_beans_drawn = allowed_children * 2  # Each allowed child drew two jelly beans
    jelly_beans_remaining = jelly_beans_in_bag - jelly_beans_drawn  # Calculate the number of jelly beans remaining

    result = jelly_beans_remaining
    return result

print(solution())