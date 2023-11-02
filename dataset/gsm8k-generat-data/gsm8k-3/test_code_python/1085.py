def solution():
    """Lily is going abroad on vacation with her family. Each of her 4 siblings is bringing 2 suitcases, and her parents are bringing 3 suitcases. Lily decides that there is already too much luggage and she won't be bringing any. How many suitcases is the entire family bringing on vacation?"""
    # Define the number of suitcases each sibling is bringing
    SIBLING_SUITCASES = 2

    # Define the number of suitcases each parent is bringing
    PARENT_SUITCASES = 3

    # Define the number of siblings and parents going on vacation
    siblings = 4
    parents = 2

    # Calculate the total number of suitcases
    total_suitcases = (siblings * SIBLING_SUITCASES) + (parents * PARENT_SUITCASES)

    # Display the total number of suitcases
    result = total_suitcases
    return result

print(solution())