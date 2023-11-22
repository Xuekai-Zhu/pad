def solution():
    
    # Define the number of clusters and the number of fruit per cluster
    clusters = 6
    fruit_per_cluster = 20

    # Calculate the total number of fruit
    total_fruit = clusters * fruit_per_cluster

    # Calculate the total number of raspberries
    total_raspberries = total_fruit * 2

    # return the result
    result = total_raspberries
    return result

print(solution())