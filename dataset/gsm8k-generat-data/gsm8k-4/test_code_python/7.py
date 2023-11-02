def solution():
    """Ken created a care package to send to his brother, who was away at boarding school. Ken placed a box on a scale, and then he poured into the box enough jelly beans to bring the weight to 2 pounds. Then, he added enough brownies to cause the weight to triple. Next, he added another 2 pounds of jelly beans. And finally, he added enough gummy worms to double the weight once again. What was the final weight of the box of goodies, in pounds?"""
    # Define the initial weight of the box (with just the jelly beans)
    weight = 2

    # Add the weight of the brownies (which triples the weight)
    weight *= 3

    # Add the weight of the second batch of jelly beans
    weight += 2

    # Add the weight of the gummy worms (which doubles the weight)
    weight *= 2

    # return the final weight in pounds
    result = weight / 16
    return result

print(solution())