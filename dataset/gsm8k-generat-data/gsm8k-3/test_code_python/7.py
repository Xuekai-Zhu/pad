def solution():
    """Ken created a care package to send to his brother, who was away at boarding school. Ken placed a box on a scale, and then he poured into the box enough jelly beans to bring the weight to 2 pounds. Then, he added enough brownies to cause the weight to triple. Next, he added another 2 pounds of jelly beans. And finally, he added enough gummy worms to double the weight once again. What was the final weight of the box of goodies, in pounds?"""
    # Define the initial weight, and the weight of the jelly beans, brownies, and gummy worms
    initial_weight = 0
    jellybean_weight = 1/3
    brownie_weight = 2/3
    gummyworm_weight = 1

    # Add the first 2 pounds of jelly beans
    initial_weight += 2

    # Add the brownies, which triple the weight
    initial_weight *= 3

    # Add the next 2 pounds of jelly beans
    initial_weight += 2

    # Add the gummy worms, which double the weight again
    initial_weight *= 2

    # Return the final weight in pounds
    result = initial_weight
    return result

print(solution())