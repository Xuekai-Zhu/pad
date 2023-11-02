def solution():
    # Calculate the total number of people in the beach house
    total_people = 8 + 6 + 4  # Karen, Donald, and their 6 children, Tom, Eva, and their 4 children

    # Calculate the total number of legs in the pool
    legs_in_pool = 16

    # Calculate the total number of legs outside the pool
    legs_outside_pool = total_people * 2 - legs_in_pool

    # Calculate the total number of people outside the pool
    people_outside_pool = legs_outside_pool // 2
    result = people_outside_pool
    return result

print(solution())