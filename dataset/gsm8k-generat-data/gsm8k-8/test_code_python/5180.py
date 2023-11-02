def solution():
    # Define the total number of kids in camp
    total_kids = 2000

    # Calculate the number of kids going to soccer camp
    soccer_kids = total_kids / 2

    # Calculate the number of kids going to soccer camp in the morning
    soccer_morning_kids = soccer_kids / 4

    # Calculate the number of kids going to soccer camp in the afternoon
    soccer_afternoon_kids = soccer_kids - soccer_morning_kids

    result = soccer_afternoon_kids
    return result

print(solution())