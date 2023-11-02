def solution():
    karen_donald_children = 6 + 2  # Karen, Donald, and their 6 children
    tom_eva_children = 4 + 2  # Tom, Eva, and their 4 children
    num_legs_in_pool = 16

    # Calculate the total number of people in the pool
    num_people_in_pool = num_legs_in_pool // 2

    # Calculate the total number of people not in the pool
    num_people_not_in_pool = karen_donald_children + tom_eva_children - num_people_in_pool
    result = num_people_not_in_pool
    return result

print(solution())