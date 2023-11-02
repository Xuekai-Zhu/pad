def solution():
    num_teachers_son = 3
    num_teachers_daughter = 4
    total_spent = 70

    # Calculate the total number of teachers to buy gifts for
    total_teachers = num_teachers_son + num_teachers_daughter

    # Calculate the cost of each gift
    gift_cost = total_spent / total_teachers
    result = gift_cost
    return result

print(solution())