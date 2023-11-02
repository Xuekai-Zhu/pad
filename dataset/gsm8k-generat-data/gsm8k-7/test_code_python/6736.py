def solution():
    num_teachers = 5
    num_friends = 14
    carnation_price = 0.5
    dozen_price = 4.0

    # Calculate the total cost of carnations for teachers
    teacher_cost = num_teachers * dozen_price / 12

    # Calculate the total cost of carnations for friends
    friend_cost = num_friends * carnation_price

    # Calculate the total cost of all carnations
    total_cost = teacher_cost + friend_cost
    result = total_cost
    return result

print(solution())