def solution():
    """Hammond carves life-sized statues out of marble. His latest set of four statues started with an 80-pound block of marble. The first statue he carved weighed 10 pounds. The second statue weighed 18. The remaining two statues weighed the same amount. The marble he discarded after carving it off the statues weighed 22 pounds. How much did each of the remaining statues Hammond carved weigh?"""
    # Define the initial weight of the marble block and weight of the discarded marble
    marble_block = 80
    marble_discarded = 22

    # Determine the weight of the first two statues combined
    first_two_statues = 10 + 18

    # Calculate the weight of the remaining two statues and subtract the weight of the discarded marble
    remaining_statues = marble_block - first_two_statues - marble_discarded
    individual_statue_weight = remaining_statues / 2

    # Display the weight of each of the remaining statues
    result = individual_statue_weight
    return result

print(solution())