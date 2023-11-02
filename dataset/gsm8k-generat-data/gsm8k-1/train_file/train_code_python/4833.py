def solution():
    """James wants to build a ladder to climb a very tall tree. Each rung of the ladder is 18 inches long and they are 6 inches apart. If he needs to climb 50 feet how many feet of wood will he need for the rungs?"""
    rung_length = 18 / 12 # converting inches to feet
    rung_spacing = 6 / 12 # converting inches to feet
    tree_height = 50
    total_rungs = (tree_height / rung_spacing) - 1 # subtracting 1 since there is no rung at the top of the ladder
    total_rung_length = total_rungs * rung_length
    result = total_rung_length
    return result

print(solution())