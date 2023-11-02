def solution():
    """A farmer living in the countryside has a certain number of children. One day, they followed him to the farm, each one with a bag to collect harvested apples. At the end of the day, each bag was filled with 15 apples each. On their way back home, 2 of the children have eaten 4 apples each and another child sold 7 of his apples. If they had a total of 60 apples left by the time they got home, how many children does the farmer have?"""
    apples_per_bag = 15
    apples_left = 60
    apples_eaten = 2 * 4
    apples_sold = 7
    total_apples = apples_left + apples_eaten + apples_sold
    children = total_apples // apples_per_bag
    result = children
    return result

print(solution())