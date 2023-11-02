def solution():
    """At the feline sanctuary, there were 12 lions, 14 tigers, and several cougars. If there were half as many cougars as lions and tigers combined, then what was the total number of big cats at the feline sanctuary?"""
    lions = 12
    tigers = 14
    cougars = (lions + tigers) / 2
    total_big_cats = lions + tigers + cougars
    result = total_big_cats
    return result

print(solution())