def solution():
    total_people = 40 + 10  # Alice's class has 40 students and 10 instructors
    students_with_life_vests = int(0.2 * 40)  # 20% of the students (8 students) are bringing life vests
    life_vests_needed = total_people - students_with_life_vests  # Alice needs life vests for everyone in the class

    # Calculate the number of additional life vests Alice needs to get
    additional_life_vests = life_vests_needed - 20
    result = additional_life_vests
    return result

print(solution())