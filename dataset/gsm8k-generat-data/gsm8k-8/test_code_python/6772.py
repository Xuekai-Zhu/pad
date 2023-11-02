def solution():
    # Calculate the total amount spent on mango juice
    mango_cost = 94 - 54
    mango_glasses = mango_cost / 5

    # Calculate the total number of glasses ordered
    total_glasses = mango_glasses + 9

    # Calculate the number of people in the group
    num_people = total_glasses / 2
    result = num_people
    return result

print(solution())