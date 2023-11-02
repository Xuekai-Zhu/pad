def solution():
    # Define the variables
    total_weight = 80
    first_statue_weight = 10
    second_statue_weight = 18
    discarded_weight = 22

    # Calculate the weight of the remaining two statues
    remaining_weight = total_weight - first_statue_weight - second_statue_weight - discarded_weight
    each_statue_weight = remaining_weight / 2

    result = each_statue_weight
    return result

print(solution())