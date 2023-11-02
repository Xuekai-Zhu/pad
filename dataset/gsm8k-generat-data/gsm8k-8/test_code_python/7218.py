def solution():
    initial_gum = 10
    additional_gum = 3
    total_friends = 11

    # Calculate how many pieces of gum were given out
    given_gum = total_friends - 1

    # Calculate how many pieces of gum Adrianna has now
    new_gum_total = initial_gum + additional_gum - given_gum

    result = new_gum_total
    return result

print(solution())