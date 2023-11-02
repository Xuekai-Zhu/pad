def solution():
    starting_apples = 25  # Sarah starts with 25 apples
    teachers_seen = 0  # Initialize the count of teachers Sarah sees to 0
    friends_given_to = 5  # Sarah gives an apple to 5 friends
    apples_eaten = 1  # Sarah eats an apple on her way home
    ending_apples = 3  # Sarah has 3 apples left when she gets home

    # Calculate the number of apples Sarah gave away to teachers
    apples_given_to_teachers = starting_apples - ending_apples - friends_given_to - apples_eaten
    result = apples_given_to_teachers
    return result

print(solution())