def solution():
    """Yanni has 5 paintings that combined, take up 200 square feet. 3 of the paintings are 5 feet by 5 feet. 1 painting is 10 feet by 8 feet. If the final painting is 5 feet tall, how wide is it?"""
    total_area = 200
    area_of_3_paintings = 3 * (5 * 5)
    area_of_1_painting = 10 * 8
    area_of_last_painting = total_area - area_of_3_paintings - area_of_1_painting
    height_of_last_painting = 5
    width_of_last_painting = area_of_last_painting / height_of_last_painting
    result = width_of_last_painting
    return result

print(solution())