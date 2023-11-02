def solution():
    """Erin counts six trolls hiding by the path in the forest, 6 less than four times that number of trolls hiding under the bridge, and half as many trolls hiding in the plains as under the bridge. How many trolls did she count in total?"""
    # Define the number of trolls by the path in the forest
    trolls_forest = 6

    # Calculate the number of trolls hiding under the bridge
    trolls_bridge = (trolls_forest + 6) / 4

    # Calculate the number of trolls hiding in the plains
    trolls_plains = trolls_bridge / 2

    # Calculate the total number of trolls
    total_trolls = trolls_forest + trolls_bridge + trolls_plains

    # return the result
    result = total_trolls
    return result

print(solution())