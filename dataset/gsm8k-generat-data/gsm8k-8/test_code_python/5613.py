def solution():
    megabytes_per_picture_1 = 8
    megabytes_per_picture_2 = 6
    total_megabytes = 3000 * megabytes_per_picture_1
    number_of_pictures = total_megabytes / megabytes_per_picture_2
    result = number_of_pictures
    return result

print(solution())