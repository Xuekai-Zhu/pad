def solution():
    """Hammond carves life-sized statues out of marble. His latest set of four statues started with an 80-pound block of marble. The first statue he carved weighed 10 pounds. The second statue weighed 18. The remaining two statues weighed the same amount. The marble he discarded after carving it off the statues weighed 22 pounds. How much did each of the remaining statues Hammond carved weigh?"""
    starting_weight = 80
    first_statue = 10
    second_statue = 18
    discarded_marble = 22
    remaining_weight = starting_weight - first_statue - second_statue - discarded_marble
    remaining_statues_weight = remaining_weight / 2
    result = remaining_statues_weight
    return result

print(solution())