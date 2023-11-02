def solution():
    """Shawna's workout goal is 30 situps. On Monday, Shawna was only able to do 12 situps, so she decided that she would make up for the rest on Tuesday. However, she was only able to do 19 situps on Tuesday. How many situps would Shawna have to do on Wednesday to meet her minimum goal and make up for the ones she didn't do?"""
    goal = 30
    monday_situps = 12
    tuesday_situps = 19
    total_situps_done = monday_situps + tuesday_situps
    situps_left = goal - total_situps_done
    result = situps_left
    return result

print(solution())