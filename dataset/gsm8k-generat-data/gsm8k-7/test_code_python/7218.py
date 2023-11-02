def solution():
    initial_gum = 10
    additional_gum = 3
    num_friends = 11

    # Calculate the total number of pieces of gum Adrianna has now
    total_gum = initial_gum + additional_gum

    # Calculate how many pieces of gum Adrianna has left after giving out to her friends
    num_gum_left = total_gum - num_friends

    result = num_gum_left
    return result

print(solution())