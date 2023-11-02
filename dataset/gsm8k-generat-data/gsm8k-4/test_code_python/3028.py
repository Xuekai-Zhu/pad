def solution():
    """There are 20 sandcastles on Mark's beach, each with 10 towers. On Jeff's beach, there are three times as many castles as on Mark's beach, each with 5 towers. What is the combined total number of sandcastles and towers on Mark's and Jeff's beaches?"""
    # Calculate the total number of towers on Mark's beach
    marks_towers = 20 * 10

    # Calculate the total number of castles on Jeff's beach
    jeffs_castles = 3 * 20

    # Calculate the total number of towers on Jeff's beach
    jeffs_towers = jeffs_castles * 5

    # Calculate the combined total number of sandcastles and towers
    total = marks_towers + jeffs_towers + jeffs_castles

    # return the result
    result = total
    return result

print(solution())