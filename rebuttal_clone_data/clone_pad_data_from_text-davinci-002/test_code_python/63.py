def solution():
     """Shawna's workout goal is 30 situps. On Monday, Shawna was only able to do 12 situps, so she decided that she would make up for the rest on Tuesday. However, she was only able to do 19 situps on Tuesday. How many situps would Shawna have to do on Wednesday to meet her minimum goal and make up for the ones she didn't do?"""
     goal = 30
     situps_done_mon = 12
     situps_done_tues = 19
     situps_needed = goal - (situps_done_mon + situps_done_tues)
     result = situps_needed
     return result

print(solution())