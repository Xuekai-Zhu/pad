def solution():
     """There are some jelly beans in a jar. Three fourths of the jelly beans are red, and one quarter of the red jelly beans are coconut flavored. If 750 jelly beans are coconut flavored, how many jelly beans are there in the jar?"""
     total_coconut_jelly_beans = 750
     coconut_percentage = 25
     red_jelly_beans = total_coconut_jelly_beans / (coconut_percentage / 100)
     total_jelly_beans = (red_jelly_beans / 4) * 3
     result = total_jelly_beans
     return result

print(solution())