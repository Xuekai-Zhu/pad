def solution():
    """Two trains leave San Rafael at the same time. They begin traveling westward, both traveling for 80 miles. The next day, they travel northwards, covering 150 miles. What's the distance covered by each train in the two days?"""
    distance_westward = 80
    distance_northward = 150
    total_distance_train1 = (distance_westward ** 2 + distance_northward ** 2) ** 0.5
    total_distance_train2 = total_distance_train1 # since both trains covered the same distance
    result = total_distance_train1 + total_distance_train2
    return result

print(solution())