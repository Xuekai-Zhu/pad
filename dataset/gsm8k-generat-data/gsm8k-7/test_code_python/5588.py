def solution():
    num_students = 40
    num_instructors = 10
    total_people = num_students + num_instructors + 1  # Add 1 for Alice
    num_life_vests_on_hand = 20
    proportion_bringing_vests = 0.2

    # Calculate the number of students bringing their own life vests
    num_students_bringing_vests = int(num_students * proportion_bringing_vests)

    # Calculate the total number of life vests needed, including those on hand
    total_life_vests_needed = num_students + num_instructors + num_students_bringing_vests

    # Calculate how many more life vests are needed
    num_additional_vests_needed = total_life_vests_needed - num_life_vests_on_hand

    result = num_additional_vests_needed
    return result

print(solution())