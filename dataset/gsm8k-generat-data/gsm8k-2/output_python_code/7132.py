def solution():
    """A farmer living in the countryside has a certain number of children. One day, they followed him to the farm, each one with a bag to collect harvested apples. At the end of the day, each bag was filled with 15 apples each. On their way back home, 2 of the children have eaten 4 apples each and another child sold 7 of his apples. If they had a total of 60 apples left by the time they got home, how many children does the farmer have?"""
    apples_per_bag = 15
    eaten_apples = 2 * 4
    sold_apples = 7
    remaining_apples = 60
    total_apples = (remaining_apples + eaten_apples + sold_apples) / (1 - 2 / (apples_per_bag * x))
    # iterate over possible number of children until the equation is satisfied
    for x in range(1, 100):
        if total_apples == (apples_per_bag * x - eaten_apples - sold_apples):
            return x

    # if no solution is found, return -1
    return -1

print(solution())