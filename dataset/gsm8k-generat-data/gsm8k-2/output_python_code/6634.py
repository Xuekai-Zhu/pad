def solution():
    """Sarah walked to school carrying a bag containing 25 apples. At school, she gave each teacher she saw an apple. She also gave a single apple to each of 5 of her closest friends. And while she walked home, she also ate one of the apples. If she had three apples left in the bag when she got home, how many apples had she given away to teachers?"""
    initial_apples = 25
    teachers = initial_apples - 3  # Sarah ate one on the way home, so she had 3 left
    friends = 5
    total_given = teachers + friends
    result = total_given
    return result

print(solution())