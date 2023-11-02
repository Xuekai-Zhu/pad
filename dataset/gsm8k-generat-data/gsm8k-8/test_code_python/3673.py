def solution():
    # Define the heights of the houses
    lucille_height = 80
    neighbor1_height = 70
    neighbor2_height = 99

    # Calculate the average height
    average_height = (lucille_height + neighbor1_height + neighbor2_height) / 3

    # Calculate how much shorter Lucille's house is than the average height
    difference = average_height - lucille_height
    result = difference
    return result

print(solution())