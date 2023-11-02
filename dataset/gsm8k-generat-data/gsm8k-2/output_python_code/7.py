def solution():
    """Ken created a care package to send to his brother, who was away at boarding school. Ken placed a box on a scale, and then he poured into the box enough jelly beans to bring the weight to 2 pounds. Then, he added enough brownies to cause the weight to triple. Next, he added another 2 pounds of jelly beans. And finally, he added enough gummy worms to double the weight once again. What was the final weight of the box of goodies, in pounds?"""
    initial_weight = 2
    jelly_beans_1 = 2
    brownies = initial_weight * 3 - initial_weight - jelly_beans_1
    jelly_beans_2 = 2
    gummy_worms = (initial_weight + jelly_beans_1 + brownies + jelly_beans_2) * 2 - (initial_weight + jelly_beans_1 + brownies + jelly_beans_2)
    final_weight = initial_weight + jelly_beans_1 + brownies + jelly_beans_2 + gummy_worms
    result = final_weight
    return result

print(solution())