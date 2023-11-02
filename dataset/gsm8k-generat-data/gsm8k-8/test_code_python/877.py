def solution():
    # Calculate the number of strawberries Kimberly's brother picked
    brother_picked = 3 * 15

    # Calculate the number of strawberries Kimberly picked
    kimberly_picked = 8 * brother_picked

    # Calculate the number of strawberries Kimberly's parents picked
    parents_picked = kimberly_picked - 93

    # Calculate the total number of strawberries picked
    total_picked = brother_picked + kimberly_picked + parents_picked

    # Calculate the number of strawberries each person gets if they divide equally
    each_person = total_picked / 4

    result = each_person
    return result

print(solution())