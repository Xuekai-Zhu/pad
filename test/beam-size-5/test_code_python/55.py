def solution():
    num_clusters = 6
    num_fruit_per_clusters = 20
    num_fruit_scattered = 67

    # Calculate the total number of fruit
    total_fruit = num_clusters * num_fruit_per_clusters

    # Calculate the total number of raspberries
    total_raspberries = total_fruit + num_fruit_scattered
    result = total_raspberries
    return result

print(solution())