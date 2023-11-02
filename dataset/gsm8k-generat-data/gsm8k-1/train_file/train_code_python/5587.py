def solution():
    """Alice's white water rafting class is composed of 40 students and 10 instructors, including herself. She has 20 life vests on hand. 20% of her students are bringing life vests. How many more life vests will Alice need to get so that entire class has one?"""
    students = 40
    instructors = 10
    alice = 1
    total_people = students + instructors + alice
    life_vests = 20
    students_with_vests = int(0.2 * students)
    total_vests = life_vests + students_with_vests
    vests_needed = total_people - total_vests
    result = vests_needed
    return result

print(solution())