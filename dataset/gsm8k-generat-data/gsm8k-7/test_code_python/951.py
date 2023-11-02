def solution():
    num_school_friends = 6
    num_neighborhood_friends = 12
    num_additional_friends_per_person = 2

    # Calculate the total number of additional friends that will come
    total_additional_friends = (num_school_friends + num_neighborhood_friends) * num_additional_friends_per_person

    # Calculate the total number of people who will be at the party
    total_people = num_school_friends + num_neighborhood_friends + total_additional_friends + 1  # add 1 for Michonne

    result = total_people
    return result

print(solution())