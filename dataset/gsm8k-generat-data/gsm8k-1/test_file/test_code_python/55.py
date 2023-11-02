def solution():
    """A raspberry bush has 6 clusters of 20 fruit each and 67 individual fruit scattered across the bush. How many raspberries are there total?"""
    clusters = 6
    cluster_size = 20
    individual_fruit = 67
    total_fruit = (clusters * cluster_size) + individual_fruit
    result = total_fruit
    return result

print(solution())