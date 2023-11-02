def solution():
    """Iris’ family is planning a surprise birthday party for her. The party will include her 3 uncles and 4 aunts who have a son and daughter each as well as her brother and mother. In total, how many people are coming to Iris’ birthday party?"""
    uncles = 3
    aunts = 4
    cousins_per_aunt_uncle = 2
    brother = 1
    mother = 1
    total_people = uncles + aunts + (uncles + aunts) * cousins_per_aunt_uncle + brother + mother
    result = total_people
    return result

print(solution())