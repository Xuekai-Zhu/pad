def solution():
    """It costs Molly $5 per package to send Christmas gifts to her relatives by mail. She has two parents and three brothers, and each of her brothers is married with 2 children each. If she sends one package to each relative by mail, how much does it cost her to send all of the gifts by mail to her relatives, in dollars?"""
    # Define the number of presents to be sent to each family member
    presents_per_person = 1

    # Define the number of parents and siblings
    parents = 2
    siblings = 3

    # Define the number of sibling's children
    children = 2
    total_children = siblings * children

    # Calculate the total number of relatives to send presents to
    total_relatives = parents + siblings + total_children

    # Calculate the total cost of sending presents to all relatives
    total_cost = total_relatives * 5

    # Return the result
    result = total_cost
    return result

print(solution())