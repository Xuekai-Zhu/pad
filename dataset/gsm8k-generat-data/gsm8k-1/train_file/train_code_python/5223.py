def solution():
    """Hammond carves life-sized statues out of marble. His latest set of four statues started with an 80-pound block of marble. The first statue he carved weighed 10 pounds. The second statue weighed 18. The remaining two statues weighed the same amount. The marble he discarded after carving it off the statues weighed 22 pounds. How much did each of the remaining statues Hammond carved weigh?"""
    total_weight = 80
    weight_of_first_statue = 10
    weight_of_second_statue = 18
    weight_of_discarded_marble = 22
    weight_of_remaining_statues = total_weight - (weight_of_first_statue + weight_of_second_statue + weight_of_discarded_marble)
    weight_of_each_remaining_statue = weight_of_remaining_statues / 2
    result = weight_of_each_remaining_statue
    return result

print(solution())