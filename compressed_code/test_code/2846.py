def solution():
    
    lucille_house = 80
    neighbor1_house = 70
    neighbor2_house = 99

    average_height = (lucille_house + neighbor1_house + neighbor2_house) / 3
    difference = average_height - lucille_house

    result = difference
    return result

print(solution())