def solution():
    """Grandma Molly created statues of turtles for her front lawn. The first year, she created 4 statues and placed them on her lawn. The second year, she quadrupled the number of statues on her front lawn. In the third year, she added another 12 statues to the front lawn, but a hail storm broke 3 of the statues, which she threw away. In the fourth year, she added twice as many new statues as had been broken the year before. At the end of the four years, how many turtle statues were on her front lawn?"""
    # Define the number of statues created in the first year
    year_1 = 4

    # Define the number of statues in the second year
    year_2 = year_1 * 4

    # Define the number of statues in the third year
    year_3 = year_2 + 12 - 3

    # Define the number of statues broken in the third year
    statues_broken = 3

    # Define the number of statues added in the fourth year
    statues_added = statues_broken * 2

    # Define the total number of statues
    total_statues = year_1 + year_2 + year_3 + statues_added

    # return the result
    result = total_statues
    return result

print(solution())