def solution():
    # Calculate the total number of sticks of wood Mary gets from the furniture
    chairs = 18  # number of chairs
    tables = 6  # number of tables
    stools = 4  # number of stools

    sticks_from_chairs = 6 * chairs  # 6 sticks of wood per chair
    sticks_from_tables = 9 * tables  # 9 sticks of wood per table
    sticks_from_stools = 2 * stools  # 2 sticks of wood per stool

    total_sticks = sticks_from_chairs + sticks_from_tables + sticks_from_stools

    # Calculate the number of hours Mary can stay warm
    hours = total_sticks / 5  # Mary needs to burn 5 sticks of wood per hour to stay warm
    result = hours
    return result

print(solution())