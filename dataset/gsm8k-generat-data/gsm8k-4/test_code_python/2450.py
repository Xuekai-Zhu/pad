def solution():
    """Jamie is a firefighter. One day an emergency call comes in from Mrs. Thompson, an elderly woman whose cat can't get down a 20-foot tree. The last time Jamie rescued a cat, he got it down from a 6-foot tree and had to climb 12 rungs of his ladder. How many rungs does he have to climb this time to get the cat down from the tree?"""
    # Define the information given in the problem
    initial_height = 6
    initial_rungs = 12
    final_height = 20

    # Calculate the ratio of height to rungs
    height_ratio = final_height / initial_height
    rungs_ratio = initial_rungs / initial_height

    # Calculate the number of rungs needed to climb the 20-foot tree
    final_rungs = height_ratio * rungs_ratio

    result = round(final_rungs)
    return result

print(solution())