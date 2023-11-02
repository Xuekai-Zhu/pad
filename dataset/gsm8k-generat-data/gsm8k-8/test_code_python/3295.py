def solution():
    # Define the number of people and children in the beach house
    karen_donald_children = 8
    tom_eva_children = 6

    # Calculate the number of adults
    num_adults = 2

    # Calculate the number of people in the pool
    num_people_in_pool = 8

    # Calculate the number of legs in the pool
    num_legs_in_pool = 16

    # Calculate the total number of people
    total_people = karen_donald_children + tom_eva_children + num_adults

    # Calculate the number of people not in the pool
    num_people_not_in_pool = total_people - num_people_in_pool

    result = num_people_not_in_pool
    return result

print(solution())