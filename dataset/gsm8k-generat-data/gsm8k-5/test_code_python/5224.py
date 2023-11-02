def solution():
    starting_weight = 80  # The block of marble started at 80 pounds
    first_statue_weight = 10  # The first statue weighed 10 pounds
    second_statue_weight = 18  # The second statue weighed 18 pounds
    discarded_weight = 22  # The weight of marble discarded after carving
    remaining_weight = starting_weight - first_statue_weight - second_statue_weight - discarded_weight  # The weight of marble remaining after carving the first two statues
    remaining_statue_weight = remaining_weight / 2  # The weight of each of the remaining two statues

    result = remaining_statue_weight
    return result

print(solution())