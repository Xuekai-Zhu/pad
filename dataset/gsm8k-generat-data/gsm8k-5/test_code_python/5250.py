def solution():
    total_people = 40  # There are 40 people in the cafeteria
    checkered_shirts = 7  # 7 people are wearing checkered shirts
    horizontal_stripes = 4 * checkered_shirts  # The number of people wearing horizontal stripes is 4 times the people wearing checkered shirts
    remaining_people = total_people - checkered_shirts - horizontal_stripes  # The remaining people are wearing vertical stripes

    result = remaining_people
    return result

print(solution())