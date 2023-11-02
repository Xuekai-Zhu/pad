def solution():
    """Alice's white water rafting class is composed of 40 students and 10 instructors, including herself. She has 20 life vests on hand. 20% of her students are bringing life vests. How many more life vests will Alice need to get so that entire class has one?"""
    # Define the total number of students and instructors
    total_people = 50

    # Define the number of life vests on hand
    vests_on_hand = 20

    # Calculate the number of students bringing life vests
    students_with_vests = 0.2 * 40

    # Calculate the remaining number of life vests needed
    vests_needed = total_people - vests_on_hand - students_with_vests

    # Return the result
    result = vests_needed
    return result

print(solution())