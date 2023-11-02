def solution():
    """Mary is chopping up some old furniture to make firewood. Chairs make 6 sticks of wood, tables make 9 sticks of wood, and stools make 2 sticks of wood. Mary needs to burn 5 sticks of wood per hour to stay warm. If Mary chops up 18 chairs, 6 tables and 4 stools, how many hours can she keep warm?"""
    # Define the number of sticks of wood produced by each type of furniture
    CHAIRS_WOOD = 6
    TABLES_WOOD = 9
    STOOLS_WOOD = 2

    # Define Mary's wood burning rate
    BURN_RATE = 5

    # Calculate the total number of sticks of wood produced
    total_wood = (18 * CHAIRS_WOOD) + (6 * TABLES_WOOD) + (4 * STOOLS_WOOD)

    # Calculate the number of hours Mary can keep warm
    hours = total_wood / BURN_RATE

    # return the result
    result = hours
    return result

print(solution())