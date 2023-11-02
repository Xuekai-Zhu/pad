def solution():
    """Ken created a care package to send to his brother, who was away at boarding school. Ken placed a box on a scale, and then he poured into the box enough jelly beans to bring the weight to 2 pounds. Then, he added enough brownies to cause the weight to triple. Next, he added another 2 pounds of jelly beans. And finally, he added enough gummy worms to double the weight once again. What was the final weight of the box of goodies, in pounds?"""
    initial_weight = 2
    weight_after_jelly_beans = initial_weight * 3
    weight_after_brownies = weight_after_jelly_beans + 2
    weight_after_gummy_worms = weight_after_brownies * 2
    final_weight = weight_after_gummy_worms
    return final_weight

print(solution())