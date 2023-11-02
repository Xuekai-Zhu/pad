def solution():
    # Calculate the distance Alex covered in the first 4.5 hours
    dist_first_leg = 20 * 4.5

    # Calculate the distance Alex covered in the next 2.5 hours
    dist_second_leg = 12 * 2.5

    # Calculate the distance Alex covered in the last 1.5 hours before the flat tire
    dist_third_leg = 24 * 1.5

    # Calculate the total distance Alex covered before the flat tire
    total_distance = dist_first_leg + dist_second_leg + dist_third_leg

    # Calculate the distance Alex had left to cover to reach the next town
    remaining_distance = 164 - total_distance

    result = remaining_distance
    return result

print(solution())