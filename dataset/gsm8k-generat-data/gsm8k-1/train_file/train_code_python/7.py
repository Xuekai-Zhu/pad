def solution():
    """Ken created a care package to send to his brother, who was away at boarding school. Ken placed a box on a scale, and then he poured into the box enough jelly beans to bring the weight to 2 pounds. Then, he added enough brownies to cause the weight to triple. Next, he added another 2 pounds of jelly beans. And finally, he added enough gummy worms to double the weight once again. What was the final weight of the box of goodies, in pounds?"""
    jelly_beans1 = 2
    brownies = jelly_beans1 * 3
    jelly_beans2 = 2
    gummy_worms = (jelly_beans1 + brownies + jelly_beans2) * 2
    total_weight = jelly_beans1 + brownies + jelly_beans2 + gummy_worms
    result = total_weight
    return result

print(solution())