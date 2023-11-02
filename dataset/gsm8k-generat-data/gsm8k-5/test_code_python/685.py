def solution():
    # Let's assume there are "x" kids in camp altogether
    total_kids = x

    # Half of the kids are going to soccer camp
    soccer_camp_kids = total_kids / 2

    # 1/4 of the kids going to soccer camp are going in the morning
    morning_soccer_kids = soccer_camp_kids / 4

    # Thus, the number of kids going to soccer camp in the afternoon is:
    afternoon_soccer_kids = 750

    # Total number of kids in camp is:
    total_kids = soccer_camp_kids + morning_soccer_kids + afternoon_soccer_kids

    return total_kids

print(solution())