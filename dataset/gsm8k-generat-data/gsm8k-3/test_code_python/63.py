def solution():
    """Shawna's workout goal is 30 situps. On Monday, Shawna was only able to do 12 situps,
    so she decided that she would make up for the rest on Tuesday. However, she was only able to do
    19 situps on Tuesday. How many situps would Shawna have to do on Wednesday to meet her minimum goal
    and make up for the ones she didn't do?"""

    # Define Shawna's workout goal
    goal = 30

    # Calculate how many situps Shawna has already done
    total_situps = 12 + 19

    # Calculate how many situps Shawna still needs to do
    remaining_situps = goal - total_situps

    # Return the number of situps Shawna needs to do on Wednesday
    result = remaining_situps
    return result

print(solution())