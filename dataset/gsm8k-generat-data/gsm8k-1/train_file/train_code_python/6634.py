def solution():
    """Sarah walked to school carrying a bag containing 25 apples. At school, she gave each teacher she saw an apple. She also gave a single apple to each of 5 of her closest friends. And while she walked home, she also ate one of the apples. If she had three apples left in the bag when she got home, how many apples had she given away to teachers?"""
    initial_apples = 25
    apples_given_friends = 5
    apples_eaten = 1
    apples_left = 3
    apples_given_teachers = initial_apples - apples_given_friends - apples_eaten - apples_left
    result = apples_given_teachers
    return result

print(solution())