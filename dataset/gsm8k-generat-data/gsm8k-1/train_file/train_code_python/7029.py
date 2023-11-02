def solution():
    """Sally was at a self-serve candy shop where you scoop candy from the bins and pay based on the weight. She scoops 32 cherry sours into a bag. Then she gets a scoop of lemon sours, and the ratio of cherry sours to lemon sours is 4:5. Then she gets a scoop of orange sours, and they make up 25% of the sours in the bag. How many sours does she have in total?"""
    cherry_sours = 32
    lemon_sours_ratio = 4/5
    lemon_sours = cherry_sours * lemon_sours_ratio
    orange_sours = 0.25 * (cherry_sours + lemon_sours)
    total_sours = cherry_sours + lemon_sours + orange_sours
    result = total_sours
    return result

print(solution())