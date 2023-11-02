def solution():
    """There are 20 sandcastles on Mark's beach, each with 10 towers. On Jeff's beach, there are three times as many castles as on Mark's beach, each with 5 towers. What is the combined total number of sandcastles and towers on Mark's and Jeff's beaches?"""
    
    # Calculate the number of towers on Mark's beach
    mark_towers = 20 * 10

    # Calculate the number of sandcastles on Jeff's beach
    jeff_castles = 3 * 20

    # Calculate the number of towers on Jeff's beach
    jeff_towers = jeff_castles * 5

    # Calculate the combined total number of sandcastles and towers
    total = mark_towers + jeff_castles + jeff_towers

    # Display the combined total
    result = total
    return result

print(solution())