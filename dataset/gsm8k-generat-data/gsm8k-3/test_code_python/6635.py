def solution():
    """Sarah walked to school carrying a bag containing 25 apples. At school, she gave each teacher she saw an apple. She also gave a single apple to each of 5 of her closest friends. And while she walked home, she also ate one of the apples. If she had three apples left in the bag when she got home, how many apples had she given away to teachers?"""
    # Define the initial number of apples in the bag
    apples = 25

    # Give away an apple to each teacher seen
    teachers_seen = 6
    apples -= teachers_seen

    # Give away an apple to each of Sarah's 5 closest friends
    friends = 5
    apples -= friends

    # Sarah ate one of the apples while walking home
    apples -= 1

    # Calculate the number of apples left in the bag when she got home
    apples_left = 3

    # Calculate the number of apples Sarah gave away to teachers
    apples_given_to_teachers = teachers_seen - apples_left

    # Display the number of apples given away to teachers
    result = apples_given_to_teachers
    return result

print(solution())