def solution():
    starting_money = 200
    mother_share = 3/8
    father_share = 3/10

    # Calculate how much money John gave to his mother
    mother_money = starting_money * mother_share

    # Calculate how much money John gave to his father
    father_money = starting_money * father_share

    # Calculate how much money John has left
    remaining_money = starting_money - mother_money - father_money
    result = remaining_money
    return result

print(solution())