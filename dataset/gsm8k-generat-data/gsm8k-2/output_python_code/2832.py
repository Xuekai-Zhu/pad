def solution():
    """Annie does a survey of the sixth-grade classes to see who prefers pretzels to goldfish. In Miss Johnson's class, 1/6 of the students preferred goldfish. In Mr. Feldstein's class, 2/3rds of the students preferred goldfish. In Ms. Henderson's class, 1/5 of the students prefer goldfish. If each class has 30 students, how many people total prefer goldfish?"""
    johnson_goldfish = 30 * (1/6)
    feldstein_goldfish = 30 * (2/3)
    henderson_goldfish = 30 * (1/5)
    total_goldfish = johnson_goldfish + feldstein_goldfish + henderson_goldfish
    result = total_goldfish
    return result

print(solution())