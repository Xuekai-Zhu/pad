def solution():
    yard_width = 200
    yard_length = 50
    sidewalk_width = 3
    sidewalk_length = 50
    flowerbed_1_width = 4
    flowerbed_1_length = 25
    flowerbed_2_width = 4
    flowerbed_2_length = 25
    flowerbed_3_width = 10
    flowerbed_3_length = 12
    flowerbed_4_width = 7
    flowerbed_4_length = 8

    # Calculate the total area of the yard
    yard_area = yard_width * yard_length

    # Calculate the area of the sidewalk
    sidewalk_area = sidewalk_width * sidewalk_length

    # Calculate the area of each flower bed
    flowerbed_1_area = flowerbed_1_width * flowerbed_1_length
    flowerbed_2_area = flowerbed_2_width * flowerbed_2_length
    flowerbed_3_area = flowerbed_3_width * flowerbed_3_length
    flowerbed_4_area = flowerbed_4_width * flowerbed_4_length

    # Calculate the total area of the flower beds
    total_flowerbed_area = flowerbed_1_area + flowerbed_2_area + flowerbed_3_area + flowerbed_4_area

    # Calculate the area of the yard not covered by the sidewalk or flower beds
    sod_area = yard_area - sidewalk_area - total_flowerbed_area

    result = sod_area
    return result

print(solution())