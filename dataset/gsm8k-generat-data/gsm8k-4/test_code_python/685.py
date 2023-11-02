def solution():
    """There are some kids in camp. Half of the kids are going to soccer camp, and 1/4 of the kids going to soccer camp are going to soccer camp in the morning. 750 kids are going to soccer camp in the afternoon. How many kids there in camp altogether?"""
    # Let's define the number of kids in the whole camp as "x"
    x = None

    # Half of the kids are going to soccer camp
    soccer_camp_kids = x / 2

    # 1/4 of the soccer camp kids are going to soccer camp in the morning
    morning_soccer_kids = soccer_camp_kids / 4

    # The rest of the soccer camp kids are going in the afternoon
    afternoon_soccer_kids = 750

    # The total number of soccer camp kids is the sum of morning and afternoon
    total_soccer_kids = morning_soccer_kids + afternoon_soccer_kids

    # The total number of kids in camp is the sum of soccer and non-soccer kids
    total_kids = x

    # We can find x by solving the equation:
    # total_soccer_kids + non_soccer_kids = total_kids
    # Substitute the values we know and solve for x
    x = 2 * total_soccer_kids
    
    result = x
    return result

print(solution())