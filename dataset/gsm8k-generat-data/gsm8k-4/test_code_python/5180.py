def solution():
    """There are 2,000 kids in camp. If half of the kids are going to soccer camp, and 1/4 of the kids going to soccer camp are going to soccer camp in the morning, how many kids are going to soccer camp in the afternoon?"""
    # Define the total number of kids in camp
    total_kids = 2000

    # Calculate the number of kids going to soccer camp
    soccer_kids = total_kids / 2

    # Calculate the number of kids going to soccer camp in the morning
    morning_kids = soccer_kids / 4

    # Calculate the number of kids going to soccer camp in the afternoon
    afternoon_kids = soccer_kids - morning_kids

    # return the result
    result = afternoon_kids
    return result

print(solution())