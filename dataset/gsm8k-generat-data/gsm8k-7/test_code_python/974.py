def solution():
    num_friends = 4
    total_muffins = 20

    # Calculate the number of muffins per person
    muffins_per_person = total_muffins / (num_friends + 1)

    result = muffins_per_person
    return result

print(solution())