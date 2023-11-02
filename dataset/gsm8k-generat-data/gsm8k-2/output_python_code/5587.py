def solution():
    """Alice's white water rafting class is composed of 40 students and 10 instructors, including herself. She has 20 life vests on hand. 20% of her students are bringing life vests. How many more life vests will Alice need to get so that entire class has one?"""
    total_people = 50  # students + instructors (including Alice)
    current_life_vests = 20
    students = 0.8 * 40  # 20% of students are bringing their own vests
    total_vests_needed = total_people - students

    additional_vests_needed = total_vests_needed - current_life_vests
    result = additional_vests_needed
    return result

print(solution())