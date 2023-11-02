def solution():
    """Iris’ family is planning a surprise birthday party for her. The party will include her 3 uncles and 4 aunts who have a son and daughter each as well as her brother and mother. In total, how many people are coming to Iris’ birthday party?"""
    uncles = 3
    aunts = 4
    cousins = (uncles + aunts) * 2
    siblings = 1 + 1  # brother and mother
    total_guests = uncles + aunts + cousins + siblings
    result = total_guests
    return result

print(solution())