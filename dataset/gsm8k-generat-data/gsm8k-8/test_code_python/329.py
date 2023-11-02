def solution():
    # Calculate the total number of doughnuts
    total_doughnuts = 2 * 12 + 3 * 12

    # Calculate the number of friends
    num_friends = 8

    # Calculate the number of doughnuts each person will receive
    doughnuts_per_person = total_doughnuts / (num_friends + 2)
    result = doughnuts_per_person
    return result

print(solution())