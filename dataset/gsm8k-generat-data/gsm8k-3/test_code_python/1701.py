def solution():
    """Sandra has a box of apples that weighs 120 pounds.  She's going to use half the weight in apples to make applesauce.  The rest will be used to make apple pies.  She needs 4 pounds of apples per pie.  How many pies will she be able to make?"""
    # Define the weight of the box of apples and the weight of apples she will use for applesauce
    box_weight = 120
    applesauce_weight = box_weight / 2

    # Calculate the weight of apples she will use for pies
    pie_weight = box_weight - applesauce_weight

    # Calculate the number of pies she can make
    pies = pie_weight / 4

    # Display the number of pies she can make
    result = pies
    return result

print(solution())