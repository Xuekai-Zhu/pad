def solution():
    initial_apples = 25
    apples_eaten = 1
    apples_given_to_friends = 5
    apples_left = initial_apples - apples_eaten - apples_given_to_friends
    apples_given_to_teachers = apples_left - 3
    result = apples_given_to_teachers
    return result

print(solution())