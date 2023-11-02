def solution():
    # Define the number of friends and muffins
    num_friends = 4
    num_muffins = 20

    # Calculate the total number of muffins each person gets
    muffins_per_person = num_muffins / (num_friends + 1)

    result = muffins_per_person
    return result

print(solution())