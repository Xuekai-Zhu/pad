def solution():
    """Sandra has a box of apples that weighs 120 pounds. She's going to use half the weight in apples to make applesauce. The rest will be used to make apple pies. She needs 4 pounds of apples per pie. How many pies will she be able to make?"""
    # Define the weight of the box of apples
    box_weight = 120

    # Calculate the weight of apples used for applesauce
    applesauce_weight = box_weight / 2

    # Calculate the weight of apples used for apple pies
    pie_weight = box_weight - applesauce_weight

    # Calculate the number of pies that can be made with the remaining apples
    pie_count = pie_weight / 4

    result = round(pie_count)
    return result

print(solution())