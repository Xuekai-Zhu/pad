def solution():
    num_apples = 25
    num_teachers = 0
    num_friends = 5

    # Give each teacher she saw an apple
    while num_apples > 0:
        num_teachers += 1
        num_apples -= 1

    # Give a single apple to each of 5 of her closest friends
    num_apples -= num_friends

    # She also ate one of the apples while walking home
    num_apples -= 1

    # Calculate how many apples she gave away to teachers
    num_apples_given_to_teachers = num_teachers - 3
    result = num_apples_given_to_teachers
    return result

print(solution())