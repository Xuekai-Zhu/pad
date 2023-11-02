def solution():
    
    lucille_height = 80
    neighbor1_height = 70
    neighbor2_height = 99
    total_height = lucille_height + neighbor1_height + neighbor2_height
    average_height = total_height / 3
    height_difference = average_height - lucille_height
    result = height_difference
    return result

print(solution())