def solution():
    """Ted the T-Rex was planning to bring potato salad to the dinosaur picnic. He knows that an adult dinosaur will eat 10 lbs of potato salad, and a child will eat half as much as an adult. If there will be 20 adults and 5 children at the picnic, how many pounds of potato salad does Ted need to bring to the picnic if he hopes to have enough to feed everyone?"""
    adult_eating = 10
    children_eating = adult_eating / 2
    total_eating = (20 * adult_eating) + (5 * children_eating)
    result = total_eating
    return result

print(solution())