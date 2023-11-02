def solution():
    """Mary is chopping up some old furniture to make firewood. Chairs make 6 sticks of wood, tables make 9 sticks of wood,
    and stools make 2 sticks of wood. Mary needs to burn 5 sticks of wood per hour to stay warm. If Mary chops up 18 chairs,
    6 tables and 4 stools, how many hours can she keep warm?"""
    # Define the number of sticks of wood produced by each type of furniture
    CHAIR_STICKS = 6
    TABLE_STICKS = 9
    STOOL_STICKS = 2

    # Define the number of each type of furniture
    num_chairs = 18
    num_tables = 6
    num_stools = 4

    # Calculate the total number of sticks of wood produced
    total_sticks = num_chairs*CHAIR_STICKS + num_tables*TABLE_STICKS + num_stools*STOOL_STICKS

    # Calculate the number of hours Mary can keep warm
    hours_keep_warm = total_sticks/5

    # Display the number of hours Mary can keep warm
    result = hours_keep_warm
    return result

print(solution())