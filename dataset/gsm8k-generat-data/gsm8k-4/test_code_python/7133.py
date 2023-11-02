def solution():
    """A farmer living in the countryside has a certain number of children. One day, they followed him to the farm, each one with a bag to collect harvested apples. At the end of the day, each bag was filled with 15 apples each. On their way back home, 2 of the children have eaten 4 apples each and another child sold 7 of his apples. If they had a total of 60 apples left by the time they got home, how many children does the farmer have?"""
    # Define the number of apples per bag and the number of apples eaten/sold by each child
    APPLES_PER_BAG = 15
    APPLES_EATEN = 4
    APPLES_SOLD = 7

    # Define the total number of apples left
    total_apples_left = 60

    # Calculate the number of children by working backwards from the total apples left
    total_children = (total_apples_left + APPLES_SOLD) / (APPLES_PER_BAG - APPLES_EATEN)

    result = int(total_children)
    return result

print(solution())