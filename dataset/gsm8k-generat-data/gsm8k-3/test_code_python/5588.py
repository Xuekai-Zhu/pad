def solution():
    """Alice's white water rafting class is composed of 40 students and 10 instructors, including herself.  She has 20 life vests on hand.  20% of her students are bringing life vests.  How many more life vests will Alice need to get so that entire class has one?"""
    # Define the number of students and instructors, and the number of life vests on hand
    students = 40
    instructors = 10
    alice = 1
    life_vests_on_hand = 20

    # Calculate the number of students bringing life vests
    students_with_vests = int(0.2 * students)

    # Calculate the total number of people who need life vests
    total_people = students + instructors + alice

    # Calculate the number of life vests needed
    vests_needed = total_people - life_vests_on_hand - students_with_vests

    # Display the number of additional life vests needed
    result = vests_needed
    return result

print(solution())