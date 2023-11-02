def solution():
    """A farmer living in the countryside has a certain number of children. One day, they followed him to the farm, each one with a bag to collect harvested apples. At the end of the day, each bag was filled with 15 apples each. On their way back home, 2 of the children have eaten 4 apples each and another child sold 7 of his apples. If they had a total of 60 apples left by the time they got home, how many children does the farmer have?"""
    # Define the number of apples in each bag
    BAG_APPLES = 15

    # Define the number of apples eaten by each child
    APPLES_EATEN = 4

    # Define the number of apples sold by one child
    APPLES_SOLD = 7

    # Define the total number of apples left after the children ate and sold some
    TOTAL_APPLES = 60

    # Calculate the total number of children
    for i in range(1, 20):
        total_apples_left = ((i * BAG_APPLES) - (2 * APPLES_EATEN) - APPLES_SOLD)
        if total_apples_left == TOTAL_APPLES:
            result = i
            return result

print(solution())