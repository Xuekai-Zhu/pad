def solution():
    """Annie does a survey of the sixth-grade classes to see who prefers pretzels to goldfish. In Miss Johnson's class, 1/6 of the students preferred goldfish. In Mr. Feldstein's class, 2/3rds of the students preferred goldfish. In Ms. Henderson's class, 1/5 of the students prefer goldfish. If each class has 30 students, how many people total prefer goldfish?"""
    # Define the number of students in each class
    CLASS_SIZE = 30

    # Calculate the number of students in each class who prefer goldfish
    johnson_goldfish = CLASS_SIZE * (1/6)
    feldstein_goldfish = CLASS_SIZE * (2/3)
    henderson_goldfish = CLASS_SIZE * (1/5)

    # Calculate the total number of students who prefer goldfish
    total_goldfish = johnson_goldfish + feldstein_goldfish + henderson_goldfish

    # Return the result
    result = total_goldfish
    return result

print(solution())