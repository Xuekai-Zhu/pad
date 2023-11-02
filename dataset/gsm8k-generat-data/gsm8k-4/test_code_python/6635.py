def solution():
    """Sarah walked to school carrying a bag containing 25 apples. At school, she gave each teacher she saw an apple. She also gave a single apple to each of 5 of her closest friends. And while she walked home, she also ate one of the apples. If she had three apples left in the bag when she got home, how many apples had she given away to teachers?"""
    # Define the initial number of apples
    initial_apples = 25

    # Define the number of apples Sarah gave to her friends
    friends_apples = 5

    # Define the number of apples Sarah ate while walking home
    eaten_apples = 1

    # Define the number of apples left when Sarah got home
    left_apples = 3

    # Calculate the number of apples Sarah gave to teachers
    given_away_apples = initial_apples - friends_apples - eaten_apples - left_apples

    # Return the result
    result = given_away_apples
    return result

print(solution())