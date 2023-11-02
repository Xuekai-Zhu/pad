def solution():
    """Yanni has 5 paintings that combined, take up 200 square feet. 3 of the paintings are 5 feet by 5 feet. 1 painting is 10 feet by 8 feet. If the final painting is 5 feet tall, how wide is it?"""
    total_area = 200
    area_covered_by_three_paintings = 3 * 25
    area_covered_by_one_painting = 10 * 8
    remaining_area = total_area - area_covered_by_three_paintings - area_covered_by_one_painting
    width_of_final_painting = remaining_area / 5
    result = width_of_final_painting
    return result

print(solution())