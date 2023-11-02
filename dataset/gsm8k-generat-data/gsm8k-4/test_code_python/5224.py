def solution():
    """Hammond carves life-sized statues out of marble. His latest set of four statues started with an 80-pound block of marble. The first statue he carved weighed 10 pounds. The second statue weighed 18. The remaining two statues weighed the same amount. The marble he discarded after carving it off the statues weighed 22 pounds. How much did each of the remaining statues Hammond carved weigh?"""
    # Define the weight of the block of marble and the weight of the discarded marble
    initial_weight = 80
    discarded_weight = 22

    # Calculate the weight of the first two statues
    first_statue_weight = 10
    second_statue_weight = 18
    total_weight_first_two = first_statue_weight + second_statue_weight

    # Calculate the weight of the remaining two statues
    remaining_weight = initial_weight - total_weight_first_two - discarded_weight
    each_remaining_weight = remaining_weight / 2

    # return the result
    result = each_remaining_weight
    return result

print(solution())