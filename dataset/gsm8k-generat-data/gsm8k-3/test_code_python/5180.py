def solution():
    """There are 2,000 kids in camp. If half of the kids are going to soccer camp, and 1/4 of the kids going to soccer camp are going to soccer camp in the morning, how many kids are going to soccer camp in the afternoon?"""
    # Calculate the number of kids going to soccer camp
    soccer_camp_kids = 2000 / 2

    # Calculate the number of kids going to soccer camp in the morning
    morning_soccer_kids = soccer_camp_kids / 4

    # Calculate the number of kids going to soccer camp in the afternoon
    afternoon_soccer_kids = soccer_camp_kids - morning_soccer_kids

    # Display the number of kids going to soccer camp in the afternoon
    result = afternoon_soccer_kids
    return result

print(solution())