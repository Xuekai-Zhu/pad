def solution():
    """Jamie is a firefighter. One day an emergency call comes in from Mrs. Thompson, an elderly woman whose cat can't get down a 20-foot tree. The last time Jamie rescued a cat, he got it down from a 6-foot tree and had to climb 12 rungs of his ladder. How many rungs does he have to climb this time to get the cat down from the tree?"""
    previous_tree_height = 6
    previous_rung_count = 12
    current_tree_height = 20
    current_rung_count = (previous_rung_count/previous_tree_height)*current_tree_height
    result = current_rung_count
    return result

print(solution())