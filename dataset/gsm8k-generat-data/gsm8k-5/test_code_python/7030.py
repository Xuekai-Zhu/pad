def solution():
    cherry_sours = 32  # Sally scoops 32 cherry sours
    lemon_sours_ratio = 4 / 5  # The ratio of cherry sours to lemon sours is 4:5
    lemon_sours = cherry_sours * lemon_sours_ratio  # The number of lemon sours Sally gets
    total_sours = cherry_sours + lemon_sours  # The total number of cherry and lemon sours
    orange_sours_ratio = 0.25  # The orange sours make up 25% of the total sours
    orange_sours = total_sours * orange_sours_ratio  # The number of orange sours Sally gets
    total_sours += orange_sours  # The total number of sours in the bag
    result = total_sours
    return result

print(solution())