def solution():
    """Grandma Molly created statues of turtles for her front lawn. The first year, she created 4 statues and placed them on her lawn. The second year, she quadrupled the number of statues on her front lawn. In the third year, she added another 12 statues to the front lawn, but a hail storm broke 3 of the statues, which she threw away. In the fourth year, she added twice as many new statues as had been broken the year before. At the end of the four years, how many turtle statues were on her front lawn?"""
    year_one = 4
    year_two = year_one * 4
    year_three = year_two + 12 - 3
    year_four = (3 * 2) + (year_three - 3)
    total_statues = year_one + year_two + year_three + year_four
    result = total_statues
    return result

print(solution())