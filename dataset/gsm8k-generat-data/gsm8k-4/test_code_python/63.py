def solution():
    """Shawna's workout goal is 30 situps. On Monday, Shawna was only able to do 12 situps, so she decided that she would make up for the rest on Tuesday. However, she was only able to do 19 situps on Tuesday. How many situps would Shawna have to do on Wednesday to meet her minimum goal and make up for the ones she didn't do?"""
    # Define Shawna's workout goal
    goal = 30

    # Calculate the total number of situps done on Monday and Tuesday
    total_situps = 12 + 19

    # Calculate the number of situps Shawna still needs to do
    remaining_situps = goal - total_situps

    # return the remaining situps
    result = remaining_situps
    return result

print(solution())