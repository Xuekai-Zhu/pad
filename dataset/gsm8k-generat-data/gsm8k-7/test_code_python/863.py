def solution():
    num_students = 25
    like_fries = 15
    like_burgers = 10
    like_both = 6

    # Calculate the number of students who only like fries
    only_fries = like_fries - like_both

    # Calculate the number of students who only like burgers
    only_burgers = like_burgers - like_both

    # Calculate the number of students who do not like either food
    neither = num_students - (only_fries + only_burgers + like_both)
    result = neither
    return result

print(solution())