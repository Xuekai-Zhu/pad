def solution():
    """James wants to build a ladder to climb a very tall tree. Each rung of the ladder is 18 inches long and they are 6 inches apart. If he needs to climb 50 feet how many feet of wood will he need for the rungs?"""
    rung_length_inches = 18
    space_between_rungs_inches = 6
    total_rung_length_inches = rung_length_inches + space_between_rungs_inches
    tree_height_feet = 50
    tree_height_inches = tree_height_feet * 12
    total_rungs_needed = tree_height_inches / total_rung_length_inches
    total_rung_length_feet = total_rungs_needed * rung_length_inches / 12
    result = total_rung_length_feet
    return result

print(solution())