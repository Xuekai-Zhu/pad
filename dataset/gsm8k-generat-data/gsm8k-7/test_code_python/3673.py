def solution():
    lucille_house_height = 80
    neighbor1_house_height = 70
    neighbor2_house_height = 99

    # Calculate the average height of all houses
    average_height = (lucille_house_height + neighbor1_house_height + neighbor2_house_height) / 3

    # Calculate how much shorter Lucille's house is compared to the average height
    difference = average_height - lucille_house_height
    result = difference
    return result

print(solution())