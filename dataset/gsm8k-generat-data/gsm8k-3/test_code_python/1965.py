def solution():
    """Grandma Molly created statues of turtles for her front lawn.  The first year, she created 4 statues and placed them on her lawn.  The second year, she quadrupled the number of statues on her front lawn.  In the third year, she added another 12 statues to the front lawn, but a hail storm broke 3 of the statues, which she threw away.  In the fourth year, she added twice as many new statues as had been broken the year before.  At the end of the four years, how many turtle statues were on her front lawn?"""
    # Year 1: 4 statues
    total_statues = 4 

    # Year 2: quadrupled number of statues
    total_statues = total_statues * 4 

    # Year 3: added 12 statues, but 3 were broken and thrown away
    total_statues += 12
    total_statues -= 3

    # Year 4: added twice as many new statues as had been broken the year before
    total_statues += 2 * 3

    # Display the total number of statues on the front lawn
    result = total_statues
    return result

print(solution())