def solution():
    """Iris’ family is planning a surprise birthday party for her. The party will include her 3 uncles and 4 aunts who have a son and daughter each as well as her brother and mother. In total, how many people are coming to Iris’ birthday party?"""
    # Define the number of uncles, aunts and their children
    uncles = 3
    aunts = 4
    children = (uncles + aunts) * 2

    # Define the number of siblings and parents attending the party
    siblings = 1
    parents = 2

    # Calculate the total number of people attending the party
    total_people = uncles + aunts + children + siblings + parents

    # return the result
    result = total_people
    return result

print(solution())