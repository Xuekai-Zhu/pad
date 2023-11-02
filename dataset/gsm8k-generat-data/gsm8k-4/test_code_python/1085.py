def solution():
    """Lily is going abroad on vacation with her family. Each of her 4 siblings is bringing 2 suitcases, and her parents are bringing 3 suitcases. Lily decides that there is already too much luggage and she won't be bringing any. How many suitcases is the entire family bringing on vacation?"""
    # Define the number of siblings and the number of suitcases per sibling
    siblings = 4
    suitcases_per_sibling = 2

    # Define the number of parents and the number of suitcases per parent
    parents = 2
    suitcases_per_parent = 3

    # Calculate the total number of suitcases
    total_suitcases = (siblings * suitcases_per_sibling) + (parents * suitcases_per_parent)

    # Return the result
    result = total_suitcases
    return result

print(solution())